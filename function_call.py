# Simple function to extract specific information in your input

import os
from openai import OpenAI
import json


client = OpenAI()


content = "I want some projects for my 3d graphics python software"
messages = [
    {
        "role": "system",
        "content": "Repository of the best opensource software and projects"
    },

    {
        "role": "user",
        "content": content,
    }
]

tools=[

    {
        "type": "function",
        "function": {
            "name": "get_top_opensource_projects",
            "description": "Get a list of top 5 open-source projects in a specified topic",
            "parameters": {
                "type": "object",
                "properties": {
                    "topics": {
                        "type": "string",
                        "description": "List of the top 5 projects "
                    }
                },
                "required": ["topics"]
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

reply_content = completion.choices[0].message
print(reply_content)
