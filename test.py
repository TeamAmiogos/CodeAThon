import openai
import re
# Set up the OpenAI API client and parameters
openai.api_key = "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"
model_engine = "davinci-codex"
max_tokens = 256

def fun(prompt):
    print("-->", prompt)
    # Generate the Python code from the API
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.5,
    n=1,
    stop=None,
    timeout=30,
    )

    generated_code = ''
    pattern = r"(?s)(^|\n)[ \t]*```python\n((?:.*?\n)+)[ \t]*```"
    # Find all matches in the text and extract the Python code
    matches = re.findall(pattern, response.choices[0].text)
    for match in matches:
        generated_code += str(match.strip())

    
    print("<----------------------------------")
    print(response.choices[0].text)
    print("---------------------------------->")
    # Print the generated Python code
    print(generated_code)


while (1):
    print("Enter your query : ", end="")
    q = input()
    prompt = "Write only function part of the code for " + q + " In python"
    fun(prompt)