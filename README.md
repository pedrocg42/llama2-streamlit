# Llama 2 with LangChain and Streamlit
The objective of this repository is to create an UI on top of the open-source Llama2 using the optimized inference in llama2.c

# Installation
In order to use this repo with Llama in the most efficient way follow the next steps:
1. Create an environment and install the requirements.txt (Note: in order to install llama-cpp-python you need a c compiler installed)
2. Download an already converted and quantized llama model from HuggingFace. You can convert it yourself but in my case I used the models from this [HuggingFace](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML) page.
3. Change the path in your .streamlit/secrests.toml file to where you have your llama model in .bin format.

And that should be all. You should be able to run this repo! :rocket:

# Run

```bash
python -m venv venv
pip install -r requirements/requirements.txt
streamlit run app.py
```