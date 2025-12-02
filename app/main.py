from fastapi import FastAPI
from app.schemas import QuestionRequest, AnswerResponse
from app.service_llm import call_llm

app = FastAPI(
    title="IsCoolGPT",
    description="Assistente inteligente de estudos em Cloud Computing",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/ask", response_model=AnswerResponse)
def ask_question(payload: QuestionRequest):
    """
    Endpoint principal do IsCoolGPT.
    Recebe disciplina e pergunta, e devolve uma resposta.
    """
    answer, model_used = call_llm(payload.subject, payload.question)
    return AnswerResponse(answer=answer, model_used=model_used)
