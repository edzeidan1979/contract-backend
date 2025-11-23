from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI(title="Backend simples do Assistente de Contratos")

# CORS liberado para testes (depois podemos restringir)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage]


class ChatResponse(BaseModel):
    reply: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Pega a última mensagem do usuário só para ecoar algo
    last = request.messages[-1].content if request.messages else ""
    reply = (
        "Backend online e funcionando.\n\n"
        f"Você perguntou: \"{last}\".\n"
        "Depois vamos trocar essa lógica pelo LLM jurídico."
    )
    return ChatResponse(reply=reply)

