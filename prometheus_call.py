# Takes a query and generates a PromQL expression. Works sometimes.

import os
from openai import OpenAI
import json


client = OpenAI()


content = "Which application is using the highest CPU across all namespaces?"
messages = [
    {
        "role": "system",
        "content": "Expert in PromQL and Kube Prometheus Stack"
    },

    {
        "role": "user",
        "content": content,
    }
]


tools = [
    {
        "type": "function",
        "function": {
            "name": "ask_database",
            "description": "Use this function to ask details about Kube Prometheus stack Prometheus application. The input should be a fully formed Prometheus PromQL query",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": f"""
                                Promql query extracting info to answer the user's question.
                                The query should be returned in plain text, not in JSON and do not encode anything similar to json. Like \\ or \ as escape characters.
                                """,
                    }
                },
                "required": ["query"],
            },
        }
    }
]


completion = client.chat.completions.create(

    messages=messages,
    model="gpt-4",
    tools= tools,
    tool_choice="auto",

)
print(completion)

# Check if the message content is None
if completion.choices[0].message.content is None:
    try:
        # Extract the tool call response
        tool_call = completion.choices[0].message.tool_calls[0]

        # Extract the arguments from the function call
        arguments_str = tool_call.function.arguments

        # Load the arguments as JSON and extract query, which contains the PromQL query
        arguments = json.loads(arguments_str)
        query_with_escapes = arguments['query']

        # Remove unnecessary escape characters
        query = query_with_escapes.replace('\\', '')

        print("Processed Query:", query)
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    # Handle the case where message content is not None
    print("Message Content:", completion.choices[0].message.content)
