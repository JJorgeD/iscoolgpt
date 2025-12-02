import os

def call_llm(subject: str, question: str) -> tuple[str, str]:
    """
    Aqui, em um cenário real, você chamaria uma API de LLM (tipo OpenAI, Groq etc).
    Neste protótipo, vou só montar uma resposta de exemplo.
    """

    model = os.getenv("LLM_MODEL_NAME", "fake-edu-llm")

    answer = (
        f"Você perguntou sobre a disciplina: {subject}.\n\n"
        f"Pergunta: {question}\n\n"
        "Esta é uma resposta gerada por um protótipo. "
        "Em produção, aqui haveria a chamada para um modelo de linguagem real."
    )

    return answer, model
