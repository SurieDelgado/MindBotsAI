from openai import OpenAI
import pyodbc
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import os

class AzureSearchHelper(): 
    def __init__(self):
        self.search_client = SearchClient(
            os.environ['azure_url'],
            "azureblob-index",
            AzureKeyCredential(os.environ['azure_apikey'])
        )

    def search_azure_captions(self, semantic_query):
    
        results = self.search_client.search(
            search_text = semantic_query,
            semantic_query = semantic_query,
            semantic_configuration_name = 'semantic content',
            query_caption = "extractive",
            query_caption_highlight_enabled = True
        )

        search_results = []
        for result in results:
            if result["metadata_storage_content_type"] != "application/pdf":
                semantic_result = { "metadata_storage_name": result["metadata_storage_name"] }
                captions = []
                for item in result["@search.captions"]:
                    item = item.as_dict()
                    captions.append({
                        "text": item['text'] if item['text'] != None else None,
                        "highlights": item['highlights'] if item['highlights'] != None else None,
                    })
                semantic_result["results"] = captions
                search_results.append(semantic_result)
        return search_results