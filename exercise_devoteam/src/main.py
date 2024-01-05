import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from src import db_context
from src.connectors import episodesConnector, commentsConnector

app = FastAPI()
db_context.start()


origins = [
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(episodesConnector.router, tags=["Episodes"],
                   prefix="/api/episodes")

app.include_router(commentsConnector.router, tags=["Comments"],
                   prefix="/api/comments")

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"Hello": "World "}



if __name__ == '__main__':
    db_context.start()
    uvicorn.run(app, port=8000)  # used to test


