from app.chatbot import ask


def aria(prompt: str, generations: int = 1, **kwargs):
    return [ask(prompt) for _ in range(generations)]