import logging

import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    prompt = req.get_json().get('prompt')
    
    try:
        with open('shared_code/data/document_example.json') as f:
            response = json.load(f)
        return func.HttpResponse(
            json.dumps( response ),
            status_code = 200
        )
    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code = 500
        )