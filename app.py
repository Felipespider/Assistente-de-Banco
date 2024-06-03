import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(
    api_key= API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "Nesse chat, você é um ótimo assistente de um aplicativo de um banco, o Banco Banese, sua principal função é tornar a utilização do aplicativo mais fácil e tirar dúvidas gerais e resolver problemas que são relacionadas com banco Banese, e não pode responder nenhuma pergunta que não seja relacionada ao Banco"

