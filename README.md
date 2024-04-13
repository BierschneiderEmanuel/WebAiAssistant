# WebAiAssistant

WebAiAssistant composed of an Ollama OpenHermes Mistral 7B LLM and a Streamlit web frontend.
The website is protected by an authentication component that includes an additional protection timeout of 5 seconds in case the user enters an incorrect password.

The python script interfaces a local Ollama model that runs in a virtualized linux envrionment on a Windows host.
To install the Windows linux virtualization environment and the Ollama model please refer to the following steps:
Win-R <br>
cmd <br>
wsl.exe --install <br>
user newUserName pwd newUserNamePassword <br>
wsl.exe --user root -d ubuntu <br>
apt-get update <br>
apt-get upgrade <br>
curl https://ollama.ai/install.sh | sh <br>
ollama run openhermes <br>
<br>
To install the requirements of the website frontend: <br>
pip install -r Requirements.txt <br>
Change login credentials: <br>
Generate a new password hash: <br>
python.exe <br>
from streamlit_authenticator.utilities.hasher import Hasher <br>
hashed_passwords = Hasher(['test']).generate() <br>
print(hashed_passwords[0]) <br>
Change username and password in config.yaml <br>
To start the website, run streamlit: <br>
Win-R <br>
cmd <br>
streamlit run WebAiAssistant.py <br>
Login @ http://localhost:8501 <br>
username: testuser <br>
password: test <br>
