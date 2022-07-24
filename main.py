from fastapi import FastAPI
import uvicorn
from app.routers import user_router



app = FastAPI(title="CRUD Básico con FastAPI",
              description="Aplicación básica creada con FastAPI",
              version="1.0.0")

app.include_router(user_router.router)

@app.get("/")
async def home():
    return {
        "message": "Hola Mundo inmundo!"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, debug=True)
