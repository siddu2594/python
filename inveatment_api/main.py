from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_home():
    """This method represnts to call to the home

    """
    return {"Hello": "world"}