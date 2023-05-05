from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
                    return{'HEllo': 'Mundo'}

# uvicorn main:app --reload

