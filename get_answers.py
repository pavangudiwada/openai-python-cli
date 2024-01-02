import os
from openai import OpenAI
import typer

app = typer.Typer()

# Use export OPENAI_API_KEY="YOUR_KEY_HERE" to set the API key as an environment variable, more details here https://github.com/openai/openai-python?tab=readme-ov-file#usage
client = OpenAI()


@app.command()
def get_answer(
    context: str = typer.Option("Professional DevOps Enginner with expert level prometheus and Kube Prometheus Stack knowledge",  help="Context for the conversation")
):


    content = typer.prompt("Ask your query: ")
    messages = [
        {
            "role": "system",
            "content": context,
        },
        {
            "role": "user",
            "content": content,
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )

    typer.echo(f"OpenAI Response: {chat_completion.choices[0].message.content}")

if __name__ == "__main__":
    app()
