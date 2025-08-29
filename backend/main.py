from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from backend import models
from backend.database import engine
# from backend.routers import 

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",       # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # ✅ Allow these origins
    allow_credentials=True,
    allow_methods=["*"],              # ✅ Allow all HTTP methods
    allow_headers=["*"],              # ✅ Allow all headers (including Authorization)
)

# app.include_router()
# app.include_router()
# app.include_router()
# app.include_router()


@app.get("/")
def root():
    return{"Hello World"}