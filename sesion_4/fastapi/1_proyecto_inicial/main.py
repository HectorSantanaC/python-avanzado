from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return "Hola desde FastAPI"

@app.get("/mi_nombre")
def get_name():
  return "Hola! Mi nombre es Héctor"