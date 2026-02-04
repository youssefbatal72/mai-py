from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hi(name: str):
    return {"message": f"Hi {name}"}


