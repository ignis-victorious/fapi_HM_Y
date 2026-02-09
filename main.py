from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
def main() -> dict[str, str]:
    return {"message": "Hello World"}
