from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get():
    return{'msg':'request received'}


#uvicorn fake_server:app --reload