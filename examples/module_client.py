import openai

# will default to `os.environ['OPENAI_API_KEY']` if not explicitly set

# all client options can be configured just like the `OpenAI` instantiation counterpart
# TODO: The 'openai.base_url' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(base_url="https://...")'
# openai.base_url = "https://..."
# TODO: The 'openai.default_headers' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(default_headers={"x-foo": "true"})'
# openai.default_headers = {"x-foo": "true"}

# all API calls work in the exact same fashion as well
stream = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)

print()
