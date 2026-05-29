import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def responder(pergunta, contexto, historico):
    prompt = f"""
Você é um assistente que responde perguntas com base em documentos.

Use:
1. O CONTEXTO dos documentos
2. O HISTÓRICO da conversa

Se a pergunta depender de algo anterior, use o histórico.

HISTÓRICO:
{historico}

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

Responda de forma clara e objetiva.
"""

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content

def resumir_video(contexto):

    prompt = f"""
Você é um especialista em resumir vídeos.

Com base no conteúdo abaixo:

{contexto}

Faça:

1. Um resumo em até 10 linhas
2. Liste os principais tópicos abordados

Seja claro e organizado.
"""

    response = client.chat.completions.create(

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content

def extrair_topicos(contexto):

    prompt = f"""
Com base no conteúdo abaixo:

{contexto}

Liste apenas os principais tópicos do vídeo.

Formato:

• tópico 1
• tópico 2
• tópico 3

Seja objetivo.
"""

    response = client.chat.completions.create(

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content