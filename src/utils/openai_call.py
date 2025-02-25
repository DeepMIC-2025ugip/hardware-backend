from typing import Generator, Type

from openai import OpenAI
from pydantic import BaseModel

from utils.settings import settings

client = OpenAI(api_key=settings.openai_api_key)


def llm_response(
    system_prompt: str,
    user_prompt: str,
    modelname: str = "gpt-4o-mini",
    json_format: bool = False,
    print_response: bool = False,
) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = client.chat.completions.create(
        model=modelname,
        messages=messages,
        response_format={"type": "json_object" if json_format else "text"},
        temperature=0.7,
        top_p=0.95,
        timeout=100,
    )

    if print_response:
        print(response.choices[0].message.content)
    return response.choices[0].message.content


def llm_response_stream(
    system_prompt: str,
    user_prompt: str,
    modelname: str = "gpt-4o-mini",
    print_response: bool = False,
) -> Generator[str, None, None]:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = client.chat.completions.create(
        model=modelname,
        messages=messages,  # type: ignore
        temperature=0.7,
        max_tokens=2000,
        top_p=0.95,
        stream=True,
        timeout=100,
    )

    for chunk in response:
        content = chunk.choices[0].delta.content  # type: ignore
        if type(content) == str:
            if print_response:
                print(content)
            yield content


def llm_response_schema(
    system_prompt: str,
    user_prompt: str,
    response_format: Type[BaseModel],
    model: str = "gpt-4o-mini",
) -> BaseModel:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=messages,
        response_format=response_format,
        timeout=100,
    )

    event = completion.choices[0].message.parsed
    return event
