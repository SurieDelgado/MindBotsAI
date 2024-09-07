from openai import OpenAI
import json
import os

class SQLGenerator(): 
    def __init__(self, prompt):
        self.client = OpenAI(api_key = str(os.environ['openai_key']))
        self.prompt = prompt
        with open('shared_code/data/metadata.json') as f:
            self.metadata = json.load(f)
    
    def generate_sql_query(self):
        
        response = self.client.completions.create(
            model = "gpt-3.5-turbo-instruct",
            prompt = f"Using the next brackets pattern: '[dbo].[table]', generate a SQL Query for the next request: '{self.prompt}' \nDatabase Metadata: {self.metadata}",
            max_tokens=2000
        )
        return response.choices[0].text