import openai
import os

import os

# Retrieve the API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
llm_model = "gpt-4o-mini"


# Create the prompt for the LLM
prompt = f"""
Imagine three different experts are answering this question.
All experts will write down 1 step of their thinking,
then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realises they're wrong at any point then they leave.
At max, each expert will write down 3 steps of their thinking before coming to a conclusion.
The question is what is the best way to make a cup of tea?
"""

# Call the OpenAI API to generate a response
response = openai.chat.completions.create(
    model=llm_model,
    messages=[{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}],
    temperature=1,  # Adjust temperature for event creativity
    max_tokens=600  # Adjust for desired event description length
)

# Retrieve the output response
output_response = response.choices[0].message.content

# Print the output response
print(output_response)