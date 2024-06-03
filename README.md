# Assistente-de-Banco

Pt-Brasil:

REQUERIMENTOS:
BAIXAR o app Postman (verificador e ambiente executador do código)
BAIXAR as bibliotecas (FASTAPI = "Criação de API", Uvicorn = "Servidor de localhost", google.generativeai = "IA"

Esse código refere-se a uma API Back-End de um assistente do Banco Banese que está apto à responder qualquer pergunta relacionada à problemas e dúvidas sobre o Banco Banese 

Usando o Google Gemini, uma IA, tivemos o apoio com respostas de prontidão para que o usuário pudesse ser respondidos de perguntas complexas, por exemplo, tornando também a imersão com o usuário mais dinâmica e prática
O Projeto Back-End foi feito em conjunto com representantes do Banco Banese, onde no permitiram criar essas soluções para os problemas que eles passam no seu site/app

Dentro do app POSTMAN, utilizando o método POST: 
O usuário, utilizando dados JSON faz perguntas ao seu critério relacionado ao Banco, e ao apertar o Send (enviar), você obtem também sua resposta no método Json
EX: 
{
    "mensagem": "Ola, se identifique por favor"
}

EXECUÇÃO:
Após instalar os requerimentos, utilize o seguinte comando no terminal da IDE ou no Prompt de Comando, cria o localhost graças ao FastAPI que disponibiliza o link com o localhost que, após o comando gerar esse código, deve ser inserido dentro do app POSTMAN:
"uvicorn main:app --reload"

POSSÍVEIS ERROS:
Se você estiver vendo o seguinte erro: ERROR:    Error loading ASGI app. Could not import module "main".
Certifique-se de que você está no diretório correto onde o arquivo main.py está localizado.

ENGLISH:

REQUIREMENTS:
DOWNLOAD the Postman app (verifier and code execution environment)
DOWNLOAD the libraries (FASTAPI = "API Creation", Uvicorn = "Localhost Server", google.generativeai = "AI"

This code refers to a Back-End API of a Banco Banese assistant who is able to answer any questions related to problems and doubts about Banco Banese 

Using Google Gemini, an AI, we had support with prompt responses so that the user could be answered complex questions, for example, also making immersion with the user more dynamic and practical.
The Back-End Project was carried out together with representatives from Banco Banese, where they allowed us to create these solutions for the problems they experience on their website/app

Within the POSTMAN app, using the POST method: 
The user, using JSON data, asks questions based on criteria related to the Bank, and when you press Send, you also get your answer in the Json method
EX: 
{
    "message": "Hello, please identify yourself"
}

EXECUTION:
After installing the requirements, use the following command in the IDE terminal or Command Prompt, it creates localhost thanks to FastAPI which provides the link with localhost which, after the command generates this code, must be inserted within the POSTMAN app:
"uvicorn main:app --reload"

POSSIBLE ERRORS:
If you are seeing the following error: ERROR: Error loading ASGI app. Could not import module "main".
Make sure you are in the correct directory where the main.py file is located.
