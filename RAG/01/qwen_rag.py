import torch
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Set prompt template for generation (optional)
from llama_index.core import PromptTemplate

def completion_to_prompt(completion):
   return f"<|im_start|>system\n<|im_end|>\n<|im_start|>user\n{completion}<|im_end|>\n<|im_start|>assistant\n"

def messages_to_prompt(messages):
    prompt = ""
    for message in messages:
        if message.role == "system":
            prompt += f"<|im_start|>system\n{message.content}<|im_end|>\n"
        elif message.role == "user":
            prompt += f"<|im_start|>user\n{message.content}<|im_end|>\n"
        elif message.role == "assistant":
            prompt += f"<|im_start|>assistant\n{message.content}<|im_end|>\n"

    if not prompt.startswith("<|im_start|>system"):
        prompt = "<|im_start|>system\n" + prompt

    prompt = prompt + "<|im_start|>assistant\n"

    return prompt

# Set Qwen2.5 as the language model and set generation config
Settings.llm = HuggingFaceLLM(
    model_name="/workspace/models/Qwen2.5-7B-Instruct-GPTQ-Int4",
    tokenizer_name="Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4",
    context_window=30000,
    max_new_tokens=2000,
    generate_kwargs={"temperature": 0.7, "top_k": 50, "top_p": 0.95},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    device_map="auto",
)

# Set embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name = "/workspace/models/bge-m3"
)

# Set the size of the text chunk for retrieval
Settings.transformations = [SentenceSplitter(chunk_size=2048)]

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./document").load_data()
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=Settings.embed_model,
    transformations=Settings.transformations
)

query_engine = index.as_query_engine()
your_query = "恶性肿瘤医疗费用保险责任"
print(query_engine.query(your_query).response)
