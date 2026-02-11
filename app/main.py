
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post,user,auth,vote

app = FastAPI()
#models.Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
#root path
@app.get("/")
def root():
    return {"message": "welcome"}




