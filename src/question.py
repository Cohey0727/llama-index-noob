from llama_index import StorageContext, load_index_from_storage
from dotenv import load_dotenv
load_dotenv()

storage_context = StorageContext.from_defaults(persist_dir='./index')
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()
answer = query_engine.query("「Djangoのクエリ改善でやった\"たった3つ\"のこと」の記事の要約をしてください。")
print(answer)
