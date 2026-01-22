from langchain_astradb import AstraDBVectorStore
from src.data_converter import Converter
from src.config import Config
from langchain_huggingface import HuggingFaceEmbeddings


class DataIngestion:
    
    def __init__(self):
        self.embedding=HuggingFaceEmbeddings(model_name=Config.EMBEDDING_MODEL)

        self.vectore =AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="filpkart",
            api_endpoint=Config.ASTRA_DB_ENDPOINT,
            token=Config.ASTRA_DB_TOKEN,
            namespace=Config.ASTRA_DB_KEY_SPACE
        )

    def ingest(self,load_existing=True):

            if load_existing:
                return self.vectore
            data=Converter(r"data\flipkart_product_review.csv").data_converter()

            self.vectore.add_documents(data)

            return self.vectore
    
if __name__=="__main__":
     ingestor=DataIngestion()
     ingestor.ingest(load_existing=False)
        
 