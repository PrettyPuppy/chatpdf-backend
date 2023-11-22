from gpt_index import GPTSimpleVectorIndex
import os
import time

os.environ["OPENAI_API_KEY"] = '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'

print(time.ctime())

index = GPTSimpleVectorIndex.load_from_disk('text.json')

print(time.ctime())

while True:

    input_text = input('Input prompt: ')
    
    response = index.query(input_text, response_mode="compact")

    print(response.response)