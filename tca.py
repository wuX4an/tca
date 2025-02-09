#!/usr/bin/env python3
import requests
import sys


def ask(ask):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "yout api key",
    }

    json_data = {
        "model": "gpt-4o-mini",
        "store": True,
        "messages": [
            {
                "role": "user",
                "content": ask,
            },
        ],
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=json_data
    )
    data = response.json()
    content = data["choices"][0]["message"]["content"]
    return content


arg = sys.argv[1:]
up = " ".join(arg)
print(ask(up))
