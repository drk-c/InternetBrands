import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

def get_summary(snippet):
    start = f"Generate a short summary to explain what this code snippet does and provide some improvements:\n\n{snippet}"


    # Using responses API instead of chat completion since recommended in SDK
    response = client.responses.create(
        model = "gpt-3.5-turbo",
        input = start
    )

    return response.output_text


if __name__ == "__main__":
    print("Type or paste your code snippet below...")
    print("Then press Ctrl+Z and Enter to trigger EOFError and finish typing\n")
    
    input_snippet = ""

    try:
        while True:
            code = input()
            input_snippet += code + "\n"
    except EOFError:
        pass

    output = get_summary(input_snippet)
    print(output)