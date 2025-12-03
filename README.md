📘 IsCoolGPT – Backend em FastAPI com LLM da Groq

Este repositório contém o backend do projeto IsCoolGPT, um microserviço desenvolvido em FastAPI, integrado ao modelo Llama 3.1 (Groq) para geração de respostas educacionais baseadas em prompts enviados pelo usuário.

O serviço expõe um endpoint principal (/ask) que recebe o assunto e a pergunta, envia para o modelo LLM e retorna uma resposta estruturada.

🚀 Tecnologias Utilizadas

Python 3.10+

FastAPI

UVicorn

Groq API (Llama 3.1)

Pydantic

Docker

iscoolgpt/
│
├── app/
│   ├── main.py              # Endpoints FastAPI
│   ├── schemas.py           # Modelos Pydantic
│   ├── service_llm.py       # Integração com Groq API
│   └── __init__.py
│
├── tests/
│   └── test_main.py         # Testes básicos
│
├── Dockerfile
├── requirements.txt
└── README.md

⚙️ Configuração do Ambiente
1. Clone o repositório
git clone https://github.com/JJorgeD/iscoolgpt.git
cd iscoolgpt

2. Crie e ative o ambiente virtual

Windows:

python -m venv venv
venv\Scripts\activate


Linux/Mac:

python3 -m venv venv
source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

4. Configure a chave da Groq

Crie um arquivo .env na raiz:

GROQ_API_KEY=sua_chave_aqui

▶️ Executando o Servidor
uvicorn app.main:app --reload


Acesse:

API: http://127.0.0.1:8000

Swagger: http://127.0.0.1:8000/docs

🧪 Endpoint Principal
POST /ask
Request
{
  "subject": "Cloud Computing",
  "question": "O que é escalabilidade?"
}

Response
{
  "answer": "Resposta gerada pelo modelo...",
  "model_used": "llama3-8b-instant"
}

🐳 Build e Execução com Docker
1. Criar imagem
docker build -t iscoolgpt .

2. Rodar container
docker run -d -p 8000:8000 --name iscoolgpt_container iscoolgpt

📦 Deploy na AWS (Opcional)

O projeto suporta deploy via:

AWS ECR (armazenamento de imagens)

AWS ECS + Fargate (execução gerenciada)

(Passo a passo pode ser adicionado se quiser.)

✔️ Status do Projeto

✔️ Backend funcional

✔️ Integração com Groq LLM

✔️ Docker configurado

✔️ Testes básicos

⬜ Melhorias futuras: autenticação, logs avançados, histórico de interações

💡 Autor

Jorge Dias
Criador do IsCoolGPT
