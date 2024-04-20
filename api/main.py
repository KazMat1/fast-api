from fastapi import FastAPI # type: ignore

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
