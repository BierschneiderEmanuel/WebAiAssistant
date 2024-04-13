# WebAiAssistant

WebAiAssistant composed of an Ollama OpenHermes Mistral 7B LLM and a Streamlit web frontend.

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
To start the website, run streamlit: <br>
Win-R <br>
cmd <br>
streamlit run website_streamlit.py <br>
