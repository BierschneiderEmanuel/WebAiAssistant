""" Copyright 2024 Emanuel Bierschneider

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. """

import subprocess
import json
import jsonstreams
import streamlit as st
import streamlit_authenticator as stauth
import numpy as np
from PIL import Image
import yaml
import time

def generate_stream_json_response(prompt):
    data = json.dumps({"model": "openhermes", "prompt": prompt})
    process = subprocess.Popen(["curl", "-X", "POST", "-d", data, "http://localhost:11434/api/generate"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    full_response = ""
    with jsonstreams.Stream(jsonstreams.Type.array, filename='./response_log.txt') as output:
        while True:
            line, _ = process.communicate()
            if not line:
                break
            try:
                record = line.decode("utf-8").split("\n")
                for i in range(len(record)-1):
                    data = json.loads(record[i].replace('\0', ''))
                    if "response" in data:
                        full_response += data["response"]
                        with output.subobject() as output_e:
                            output_e.write('response', data["response"])
                    else:
                        return full_response.replace('\0', '')
                if len(record)==1:
                    data = json.loads(record[0].replace('\0', ''))
                    if "error" in data:
                        full_response += data["error"]
                        with output.subobject() as output_e:
                            output_e.write('error', data["error"])
                return full_response.replace('\0', '')
            except Exception as error:
                # handle the exception
                print("An exception occurred:", error)
    return full_response.replace('\0', '')

def main():  
    css = '''
    <style>
    .chat-message 
    {
        padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
    }
    .chat-message.user
    {
        background-color: #bbc4c3
    }
    .chat-message.bot 
    {
        background-color: #969fb0
    }
    .chat-message.avatar
    {
        width: 15%;
    }
    .chat-message.avatar img 
    {
        max-width: 32px;
        max-height: 50px;
        border-radius: 50%;
        object-fit: cover;
    }
    .chat-message.message 
    {
        width: 75%;
        padding: 0 1rem;
        color: #fff;
    }
    .stApp 
    {
        margin: auto;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        overflow: auto;
        background: black;
        background-size: 100%;
        background-attachment: fixed;
    }
    </style>
    '''

    st.set_page_config(page_title="WebAiAssistant", page_icon=":chatbot:")
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=yaml.loader.SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    name, authentication_status, username = authenticator.login('main', fields = {'Form name': 'WebAiAssistant Login'})
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        image_a = Image.open("a.png")
        image_q = Image.open("q.png")
        response = ""
        st.write(css, unsafe_allow_html=True)
        st.title("WebAiAssistant")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if prompt := st.chat_input("<->"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user", avatar=np.array(image_q)):
                st.markdown(prompt)
            with st.chat_message("assistant", avatar=np.array(image_a)):
                response = st.write(generate_stream_json_response("<|im_start|>user" + '\n' + prompt + "<|im_end|>"))
            st.session_state.messages.append({"role": "assistant", "content": response})
    elif st.session_state["authentication_status"] == False:
        time.sleep(5)
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        time.sleep(5)
        st.warning('Please enter your username and password')

if __name__ == "__main__":
    main()