# You will be prompted to enter a query and a response will be displayed in the terminal itself.

import os
from openai import OpenAI
import typer

app = typer.Typer()

# Use export OPENAI_API_KEY="YOUR_KEY_HERE" to set the API key as an environment variable, more details here https://github.com/openai/openai-python?tab=readme-ov-file#usage
client = OpenAI()


@app.command()
def get_answer(
    role: str = typer.Option("Professional DevOps Engineer with expert level Prometheus and Kube Prometheus Stack knowledge",  help="AI context for the conversation")
):


    content = typer.prompt("Ask your query: ")
    messages = [
        {
            "role": "system",
            "content": role,
        },
        {
            "role": "user",
            "content": content,
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4",
    )

    typer.echo(f"OpenAI Response: {chat_completion.choices[0].message.content}")

if __name__ == "__main__":
    app()
