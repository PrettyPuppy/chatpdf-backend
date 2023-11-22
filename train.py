from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = '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'

max_input_size = 4096
num_outputs = 1240
max_chunk_overlap = 20
chunk_size_limit = 600

prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

documents = SimpleDirectoryReader(R'source\mobile').load_data()

index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

index.save_to_disk('mobile.json')
