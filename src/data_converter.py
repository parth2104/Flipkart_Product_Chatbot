import pandas as pd
from langchain_core.documents import Document 

class Converter:
    def __init__(self,file_path:str):
        self.file_path=file_path
    
    def data_converter(self):

        df=pd.read_csv(self.file_path)[["product_title","review"]]

        documents = [Document(
                        page_content=review,    
                        metadata={"product_title": title})
                        for review, title in zip(df["review"], df["product_title"])]
        return documents