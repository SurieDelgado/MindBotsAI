import logging
import azure.functions as func
import json
from shared_code.document_utils.azure_search import AzureSearchHelper
from shared_code.document_utils.gpt_document import GPTDocumentUtils

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    prompt = req.get_json().get('prompt')
    
    try:
        azure_utils = AzureSearchHelper()
        gpt_utils =  GPTDocumentUtils()

        semantic_query = gpt_utils.generate_semantic_query(prompt)
        results = azure_utils.search_azure_captions(semantic_query)
        response = gpt_utils.generate_nl_response(prompt, [result["results"] for result in results])
        
        return func.HttpResponse(
            json.dumps( {
                "nl_response" : response,
                "semantic_results": results
            }),
            status_code = 200
        )
    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code = 500
        )