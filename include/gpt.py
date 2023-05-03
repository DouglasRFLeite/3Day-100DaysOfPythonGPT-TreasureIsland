import openai

def get_completion(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        model=model,
        prompt = prompt,
        max_tokens = 2048,
        temperature=1, # this is the degree of randomness of the model's output
    )
    return response.choices[0].text