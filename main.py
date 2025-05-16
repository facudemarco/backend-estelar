from fastapi import FastAPI
import uvicorn
from models.product import Product
from routers.product import router as routerProduct
from routers.destacados import router as routerDestacados
from routers.cartelera import router as routerCartelera
# from routers.login import router as routerLogin
from routers.contact import router as routerContact
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://estelarviajes.com",
    "estelar-viajes-website.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {"message": "Estelar Viajes API by iWeb Techonology. All rights reserved"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# app.include_router(routerLogin)

app.include_router(routerProduct)
app.include_router(routerDestacados)
app.include_router(routerCartelera)
app.include_router(routerContact)