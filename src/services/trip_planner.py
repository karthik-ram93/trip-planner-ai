import json
import logging
import pprint
from configs.prompts import *
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from constants.app_constants import USER_ROLE,ASSISTANT_ROLE
from models.llm_model import OllamaModel
from data.vector_store import FaiisVectorStore
from langchain.vectorstores.base import VectorStoreRetriever
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from services.output_processor import OutputProcessor

class TripPlanner:
    def __init__(self):
        # Use the latest system prompt
        self.system_prompt = TRAVEL_ASSISTANT_SYSTEM_PROMPT_V4
        # Initialize LLM using OllamaModel class
        llm_instance = OllamaModel()
        self.llm_model = llm_instance.get_chat_instance()
        # Initialize vector store and retriever
        self.vector_store = FaiisVectorStore().get_vector_store()
        # Maintain message history as a list of LangChain messages
        self.message_history = []

        self.generic_docs = self.vector_store.similarity_search('General Offers (All Destinations)', k=1)
        print(f'Generic Docs: {self.generic_docs}')

    def get_response(self, user_query):
        """
        Given a user query, updates message history and returns the assistant's response using RAG.
        """
        # Add user message to history
        self.construct_messages(user_query, USER_ROLE)

        # Retrieve 2 relevant chunks from vector store with L2 score (lower is more similar)
        filtered_docs_with_score = self.vector_store.similarity_search_with_score(user_query, k=2, score_threshold=0.7)
        filtered_docs = [doc for doc, score in filtered_docs_with_score]
        if not filtered_docs:
            logging.warning(f"No relevant documents found for query: {user_query}")
            filtered_docs = self.generic_docs

        # Use filtered documents for RAG context
        rag_context = "\n".join([doc.page_content for doc in filtered_docs])
        if not rag_context:
            rag_context = "No specific offers found for your query. I can still help you plan your trip."

        print(f'RAG Context: {rag_context}')

        # Update the system message with the latest context
        formatted_prompt = self.system_prompt.format(
            context=rag_context
        )
        
        system_message =  [SystemMessage(content=formatted_prompt)]

        # Get LLM response
        response = self.llm_model.invoke(system_message + self.message_history)
        processed_response = OutputProcessor.process_response(response)
        # print(f'LLM Response: {processed_response}')
        # Add assistant message to history
        self.construct_messages(processed_response, ASSISTANT_ROLE)
        return processed_response

    def construct_messages(self, content, role):
        """
        Constructs and appends a message to the message history with the given role.
        """
        if role == USER_ROLE:
            message = HumanMessage(content=content)
        elif role == ASSISTANT_ROLE:
            message = AIMessage(content=content)
        else:
            raise ValueError("Invalid role. Use 'user' or 'assistant'.")
        self.message_history.append(message)
        return self.message_history
