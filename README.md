# WebAiAssistant

WebAiAssistant is an AI assistant that is composed of an Ollama OpenHermes Mistral 7B LLM and a Streamlit web frontend. <br>
One could easily deploy this website to a cloud endpoint using the Streamlit's cloud deployment functionality. <br>
The website is protected by an authentication component that includes an additional protection timeout of 5 seconds in case the user enters an incorrect password. <br>
New usernames and passwords can be added to the config.yaml file. <br>
The python script interfaces a local Ollama model that runs in a virtualized linux envrionment on a Windows host. <br>
To install the Windows linux virtualization environment and the Ollama model please refer to the following steps: <br>
![IMG_4148](https://github.com/BierschneiderEmanuel/WebAiAssistant/assets/77926785/892be6c6-04fb-4c45-9ee9-695db111fa91)
![IMG_4149](https://github.com/BierschneiderEmanuel/WebAiAssistant/assets/77926785/19750948-400f-4e2b-b2d6-93a78d1c9261)
![IMG_4147](https://github.com/BierschneiderEmanuel/WebAiAssistant/assets/77926785/351e4e53-15e5-453e-895a-9e94b5b52f26)
![IMG_4150](https://github.com/BierschneiderEmanuel/WebAiAssistant/assets/77926785/24435235-b58b-4d3a-b08f-7139e690c403)

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
