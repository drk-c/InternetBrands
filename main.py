import os
from openai import OpenAI

client = OpenAI()

def get_summary(snippet):
    start = f"Generate a short summary to explain what this code snippet does and provide some improvements:\n\n{snippet}"


    # Using responses API instead of chat completion since recommended in SDK
    response = client.responses.create(
        model = "gpt-4o-mini",
        input = start
    )

    return response.output_text


if __name__ == "__main__":
    input_snippet = ""

    try:
        while True:
            code = input()
            input_snippet += code + "\n"
    except EOFError:
        pass

    output = get_summary(input_snippet)
    print(output)