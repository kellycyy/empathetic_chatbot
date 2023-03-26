from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os
from langchain import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import openai

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--input', required=True)
# args = parser.parse_args()

# seeker_post = args.input

template = """Imagine that you are a Reddit user who wants to respond empathetically to a post about someone's situation. \n \
            The following is an example of a reddit post and its empathetic response.\n 
            Post: {sample_seeker_post}\n Response: {sample_responder_post}\n Post: {seeker_post} \n Response:"""


prompt = PromptTemplate(
        template=template,
        input_variables=['sample_seeker_post', 'sample_responder_post', 'seeker_post']
)

prompt_short = PromptTemplate(template='{input}', input_variables=['input'])

#davinci = OpenAI(model_name="text-davinci-003")
davinci = ChatOpenAI(model_name="gpt-3.5-turbo")
davinci = ChatOpenAI(model_name="gpt-4")
embeddings = OpenAIEmbeddings()

llm_chain = LLMChain(
    prompt=prompt,
    llm=davinci
)

llm_chain_short = LLMChain(
    prompt=prompt_short,
    llm=davinci
)

faiss = FAISS.load_local('empathetic_index_weak_filter', embeddings)


# print(similar_docs)
# print(similar_docs[0].page_content)
# print(similar_docs[0].metadata['responder_post'])

def get_response(seeker_post):
    similar_docs = faiss.similarity_search(seeker_post, k=1)

    input_example = {
        'sample_seeker_post': similar_docs[0].page_content,
        'sample_responder_post': similar_docs[0].metadata['responder_post'],
        'seeker_post': seeker_post
    }
    response = None
    toxic = False 
    while response is None or toxic:
        print("trying a request", response, toxic)
        response = llm_chain.run(input_example) if len(seeker_post) > 15 else llm_chain_short.run({'input':seeker_post})
        toxic = openai.Moderation.create(input=response)["results"][0]["flagged"]
    return response


if __name__ == '__main__':
    seeker_post = "Hello"
    responder_answer = get_response(seeker_post)
    print(responder_answer)
    # response = openai.Moderation.create(
    #     input=""
    # )
    # output = response["results"][0]
    # print(response)