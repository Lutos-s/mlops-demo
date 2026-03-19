from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "hello mlops"}

@app.get("/health")
def health():
    return {"status": "ok"}