from db.products_db import ProductsInDB
from db.products_db import save_product, get_product, delete_product

from models.product_models import ProductIn, ProductOut, ProductCreate

from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
<<<<<<< HEAD
    "http://localhost", "http://localhost:8080", "https://mygicapp.herokuapp.com",
=======
    "http://localhost", "http://localhost:8080",
    "http://127.0.0.1:8000", "https://mygicapp.herokuapp.com",
>>>>>>> ba9955a67ad7d905c7b3cf1d55948f137b0b3dd7
    "https://app-mygic.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/product/")
async def create_product(product_create: ProductCreate):
    #Totas las comprobaciones Necesarias
    product_creado = get_product(product_create.codigo)

    if product_creado != None:        
        raise HTTPException(status_code= 400, detail= "El producto ya existe")
    
    producto_guardado = save_product(ProductsInDB(**product_create.dict()))
    producto = ProductOut(**producto_guardado.dict())
    #product_saved = save_product(ProductsInDB(**product_creado.dict()))
    return producto



@api.get("/product/{codigo}")
async def get_producto(codigo: str):

    product_in_db = get_product(codigo)

    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")

    product_out = ProductOut(**product_in_db.dict())

    return product_out
<<<<<<< HEAD

@api.put("/product/")
async def update_product(product_create: ProductCreate):
    product_in_db = get_product(product_create.codigo)

    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no encontrado")

    product_updated = save_product(ProductsInDB(**product_create.dict()))

    return ProductOut(**product_updated.dict())

@api.delete("/product/{codigo}")
async def delete_product_codigo(codigo: str):
    product_in_db = get_product(codigo)

    if product_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no encontrado")

    product_deleted = delete_product(codigo)

    return ProductOut(**product_deleted.dict())

    
=======
>>>>>>> ba9955a67ad7d905c7b3cf1d55948f137b0b3dd7
