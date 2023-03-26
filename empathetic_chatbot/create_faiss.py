from langchain import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pandas as pd 
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()


df = pd.read_csv("data-all-level.csv")


seeker_posts = list(df['seeker_post'])
responder_posts = list(df['response_post'])
weak_filter = list(df['weak'])

seeker_posts = [seeker_posts[i] for i in range(len(weak_filter)) if weak_filter[i]]
responder_posts = [responder_posts[i] for i in range(len(weak_filter)) if weak_filter[i]]

# seeker_posts = ['dog', 'cat', 'cow', 'sheep']
# responder_posts = ['puppy', 'kitten', 'foal', 'kid']

metadatas = [{'responder_post': responder_post} for responder_post in responder_posts]

faiss = FAISS.from_texts(seeker_posts, embeddings, metadatas=metadatas)
faiss.save_local('empathetic_index_weak_filter')

similar_docs = faiss.similarity_search("Hi how are you doing", k=1)

print(similar_docs)
