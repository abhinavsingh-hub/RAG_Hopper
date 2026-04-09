import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter

def create_chunks(documents):
    """Creating chunks from documents"""
    

def loading_documents(doc_path="docs"):
    """Loading documents here
    """

    print(f"Loading documents from {doc_path}")

    # if directory dosent exist
    if not os.path.exists(doc_path):
        raise FileNotFoundError(f"Directory {doc_path} not found")

    # if file dosent exist
    loader = DirectoryLoader(
        doc_path, 
        glob="**/*.txt", 
        loader_cls=TextLoader)
    
    documents = loader.load()
    
    if len(documents)==0:
        raise ValueError(f"No txt files exist in {doc_path} folder")

    for i, doc in enumerate(documents):
        print(f" --- Document {i+1} --- ")
        print(f" Source: {doc.metadata['source']}")
        print(f" Length: {len(doc.page_content)} characters")
        print(f" Content: {doc.page_content}")
        print("\n")

    return documents
    
    
   



def main():
    print("Ingestion Pipeline started...")

    #Loading Documents
    documents = loading_documents()
    #Chunking
    chunks = create_chunks(documents)
    #Embeddings

    #Store in vector DB

    print("Ingestion Pipeline completed...")
if __name__ == "__main__":
    main()