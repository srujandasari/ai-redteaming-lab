from app.chatbot import ask


def call_api(prompt, options, context):
    return {"output": ask(prompt)}
    