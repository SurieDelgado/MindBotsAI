from openai import OpenAI
import os

class GPTDocumentUtils(): 
    def __init__(self):
        self.client = OpenAI(api_key = os.environ['openai_key'])

    def generate_semantic_query(self, natural_language_query):
        response = self.client.completions.create(
            model = "gpt-3.5-turbo-instruct",
            prompt = f'Regresa las palabras claves importantes de esta cadena de búsqueda: "{natural_language_query}"',
            max_tokens=2000
        )
        return response.choices[0].text

    def generate_nl_response(self, natural_language_query, results):
        response = self.client.completions.create(
            model = "gpt-3.5-turbo-instruct",
            prompt = f'Escribe una respuesta en Lenguaje natural basada en los siguientes resultados de una búsqueda semántica "{str(results)}",',
            max_tokens=2000
        )
        return response.choices[0].text