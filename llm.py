from __future__ import annotations

from openai import OpenAI

from config import get_openai_base_url, get_openai_model, require_openai_api_key


def get_client() -> OpenAI:
    return OpenAI(
        api_key=require_openai_api_key(),
        base_url=get_openai_base_url(),
    )


def chat(messages, tools=None):
    response = get_client().chat.completions.create(
        model=get_openai_model(),
        messages=messages,
        tools=tools
    )
    return response
