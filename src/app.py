from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.llm_chain import create_chain
from langserve import add_routes
from src.config import MODEL_TYPE_GEMINI
from src.data_models import AdolescentInput
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  title="Peer match service ",
  version="1.0",
  description="AI powered peer match service for mental health",
)

origins = [
    "http://localhost:4200",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(app, create_chain(MODEL_TYPE_GEMINI), path="/peer-match", input_type=AdolescentInput)
