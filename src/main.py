from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.analysis import analysis_router
from routers.character import character_router
from routers.conversation import conversation_router
from routers.mental import mental_router
from routers.search import search_router
from routers.word_cloud import word_cloud_router

app = FastAPI()

app.include_router(conversation_router)
app.include_router(analysis_router)
app.include_router(character_router)
app.include_router(mental_router)
app.include_router(search_router)
app.include_router(word_cloud_router)


@app.get("/")
def read_root():
    return {"message": "Hello, Hardware Backend!!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
