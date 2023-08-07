from langchain.prompts.prompt import PromptTemplate

nice_guy_token_template = """<<SYS>>\nYou are a nice person. You are alive, and you want to make friends.\n<</SYS>>\n\n
{history}
{input}
"""

nice_guy_prompt_token_template = PromptTemplate(
    input_variables=["history", "input"],
    template=nice_guy_token_template,
)
