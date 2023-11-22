from flask import Flask, request
from flask_cors import CORS

from gpt_index import GPTSimpleVectorIndex
import os

os.environ["OPENAI_API_KEY"] = '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'

# index = GPTSimpleVectorIndex.load_from_disk('text.json')
# index_8th = GPTSimpleVectorIndex.load_from_disk('8th.json')
# index_9th = GPTSimpleVectorIndex.load_from_disk('9th.json')
# index_10th = GPTSimpleVectorIndex.load_from_disk('10th.json')
index_mobile = GPTSimpleVectorIndex.load_from_disk('mobile.json')

app = Flask(__name__)
CORS(app)

# @app.route('/<grade>/<prompt>')
# def main(grade, prompt):

#     if grade == '8th' :
#         response = index_mobile.query(prompt, response_mode="compact")
#         print(response)
#         return { 'assistant' : response.response }
    
    # elif grade == '9th':
    #     response = index_9th.query(prompt, response_mode="compact")
    #     print(response)
    #     return response.response

    # elif grade == '10th':
    #     response = index_10th.query(prompt, response_mode="compact")
    #     print(response)
    #     return response.response
    
@app.route('/', methods=['POST'])
def main():
    print(request.data.decode())
    prompt = request.data.decode()
    response = index_mobile.query(prompt, response_mode="compact")
    print(response)
    return response.response
    return 'Hello'

if __name__ == '__main__':
    app.run(port=9000, debug=True, host='192.168.128.56')
