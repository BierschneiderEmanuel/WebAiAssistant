# WebAiAssistant-
WebAiAssistant composed of an Ollama OpenHermes Mistral 7B LLM and a Streamlit web frontend

The python script interfaces a local Ollama model that runs in a virtualized linux envrionment on a Windows host.
To install the Windows linux virtualization environment and the Ollama model please refer to the following steps:
Win-R
cmd
wsl.exe --install
user newUserName pwd newUserNamePassword
wsl.exe --user root -d ubuntu
apt-get update
apt-get upgrade
curl https://ollama.ai/install.sh | sh
ollama run openhermes

To start the voice assistant run the python script:
Win-R
cmd
python voiceAiAssistant.py 

Install requirements:
pip install -r Requirements.txt

Run:
streamlit run website_streamlit.py
