from legal_research_assistant import DHARA
import os
import modal

# Initialize the LegalResearchAssistant class

assistant = DHARA(
    hf_token=os.environ['HF_TOKEN'], 
    model_id="mistralai/Mistral-7B-Instruct-v0.2", 
    embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"
)



# Load documents
documents = assistant.load_text_files('data_summary')

response = assistant.run_query(documents, question)
