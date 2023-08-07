# Llama 2 with LangChain and Streamlit
The objective of this repository is to create an UI on top of the open-source Llama2 using the optimized inference in llama2 provided by llama2.c or llama.cpp repositories. 

# Installation
In order to use this repo with Llama2 in the most efficient way follow the next steps:
1. Create a Python environment (I used Python 3.10 in my case) and install the requirements.txt (Note: in order to install llama-cpp-python you need a c compiler installed)
2. In order for [llama.cpp](https://github.com/ggerganov/llama.cpp) to be executed you need the model weights converted in a specific format. You can follow the steps in their README to do so or you can download an already converted and quantized llama2 model from HuggingFace. In my case I used the models from this [HuggingFace](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML) page.
3. Change the path in your .streamlit/secrets.toml file to where you have your llama model in .bin format.

And that should be all. You should be able to run this repo! :rocket:

# Run

```bash
python -m venv venv
pip install -r requirements/requirements.txt
streamlit run app.py
```
