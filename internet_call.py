# Identifies a website in your query, looks it up and returns a response based on your initial query

import os
from openai import OpenAI
import json
import requests
from bs4 import BeautifulSoup


client = OpenAI()



def get_information(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return "Error fetching the website."

def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Example: Targeting article tags specifically
    articles = soup.find_all('article')
    if articles:
        return ' '.join(article.get_text(separator=' ', strip=True) for article in articles)

    # Fallback: Extract text from body if no article tags are found
    body = soup.find('body')
    if body:
        # Exclude script and style elements
        for script_or_style in body(['script', 'style']):
            script_or_style.decompose()

        return body.get_text(separator=' ', strip=True)

    return "No relevant text found."


user_prompt = "summarize whats on www.theverge.com/tech into a bedtime story for a navi child on pandora"    # You're question here


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_information",
            "description": "Use this function if a user asks for information about a website and gives you the name of the website",
            "parameters": {
                "type": "object",
                "properties": {
                    "website": {
                        "type": "string",
                        "description": f"""
                                Name of the website which the user wants information about. You should strictly return the website as https://website.com. Add https:// if not already present.
                                """,
                    }
                },
                "required": ["website"],
            },
        }
    }
]


completion = client.chat.completions.create(

    messages=[{ "role": "user", "content": user_prompt}],
    model="gpt-4",
    tools= tools,
    tool_choice="auto",

)

# Check if the message content is None
if completion.choices[0].message.content is None:
    try:
        # Extract the tool call response
        tool_call = completion.choices[0].message.tool_calls[0]

        # Extract the arguments from the function call
        arguments_str = tool_call.function.arguments

        arguments = json.loads(arguments_str)
        website = arguments['website']

        print("Processed Website:", website)


    except Exception as e:
        print(f"An error occurred: {e}")
else:
    # Handle the case where message content is not None
    print("Message Content:", completion.choices[0].message.content)

if tool_call.function.name == "get_information":
    html_content = get_information(website)
    if not html_content == "Error fetching the website.":
        content = extract_text(html_content)

        if not content == "No relevant text found.":

            second_completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": user_prompt},
                    {"role": "function", "name": tool_call.function.name, "content": content},
                ],
                tools=tools,
                tool_choice="auto",

            )
            response = second_completion.choices[0].message.content
            print(response)
else:
    print("I'm clueless")