from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.crud import crud_router

app = FastAPI()

app.include_router(crud_router)


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
