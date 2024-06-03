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

