import logging

import azure.functions as func

from shared_code.sql_utils.execute_sql import SQLExecutor
from shared_code.sql_utils.generate_sql import SQLGenerator
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    prompt = req.get_json().get('prompt')
    
    try:
        query = SQLGenerator(prompt).generate_sql_query()
        data = SQLExecutor().execute_query(str(query))
        return func.HttpResponse(
            json.dumps( {
                "prompt": prompt,
                "query": query,
                "db_result": data
            }),
            status_code = 200
        )
    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code = 500
        )
