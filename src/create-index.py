from llama_index import GPTVectorStoreIndex, SimpleWebPageReader
from dotenv import load_dotenv
load_dotenv()

article_urls = [
    'https://qiita.com/cohey0727/items/554f02a299ed65ff2db8',
]

documents = SimpleWebPageReader().load_data(article_urls)
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir='./index')
