from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"meggage" : "Hello World"}