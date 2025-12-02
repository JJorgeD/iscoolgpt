from pydantic import BaseModel

class QuestionRequest(BaseModel):
    subject: str
    question: str

class AnswerResponse(BaseModel):
    answer: str
    model_used: str
