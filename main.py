print("main.py está sendo executado")

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app import *  


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chatbot")
async def conversar(request: Request):
    request_data = await request.json() #JSON 
    question = request_data["mensagem"]  #Mensagem
    response = chat.send_message(question + instruction)  #Resposta através do = Chat + função enviar_msg (pergunta + instruc)
    return {"Chatbot": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
