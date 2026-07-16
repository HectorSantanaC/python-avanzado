from fastapi import FastAPI

app = FastAPI()

@app.get("/productos")
def listar_productos():
  return {"productos": ["Laptop", "Smartphone", "Tablet"] }