from fastapi import FastAPI

""" - import FastAPI;
- create a FastAPI application object;
- define one HTTP GET route for /;
- return this JSON-compatible data:
{"message": "Hello World"}
 """

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}
