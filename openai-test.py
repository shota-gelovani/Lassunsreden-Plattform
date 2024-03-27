from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a funny comedian who tells dad jokes. The output should be in html format."},
    {"role": "user", "content": "Write a dad joke related to numbers."},
    {"role": "assistant", "content": "Q: How do you make 7 even? A: Take away the s."},
    {"role": "user", "content": "Write one related to programmers."}
  ]
)

print(completion.choices[0].message)


  