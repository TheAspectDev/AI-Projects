from fastapi.params import Body
from main import predict
import numpy as np
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/check")
def read_item(body = Body()):
    print(body)
    return str(predict(np.array([json.loads(body)['shape']])))