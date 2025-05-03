from fastapi import APIRouter, HTTPException
from models.product import Product
from Database.dbGetConnection import getConnection
from Database.testConnection import get_connection
import uuid


router = APIRouter()

@router.get('/teste-database')

def testeDatabase():
    connection = get_connection()
    return {"message": "Database connection successful"}

# Get all products

@router.get('/products')

def getProducts():
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `Products`")

    products = cursor.fetchall()
    cursor.close()

    connection.close()
    return products
    
# Filter products by id

@router.get('/products/{id}')

def getProduct(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `Products` WHERE id = %s", (id,))

    product = cursor.fetchone()
    cursor.close()

    connection.close()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

# Crear producto
@router.post('/products/create_product')

def createProduct(product: Product):

    connection = getConnection()

    generated_id = str(uuid.uuid4())

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO `Products`(`ID`, `destino`, `subtitulo`, `date`, `date2`, `date3`, `days`, `nights`, `regimen`, `transporte`, `periodo`, `paquete`, `descripcion`, `moneda`, `precio`, `adicional`, `image`, `desde`, `hotel`, `incluye`, `incluye2`, `incluye3`, `incluye4`, `observaciones`, `observaciones2`, `observaciones3`, `itinerario`, `itinerario2`, `itinerario3`, `itinerario4`, `itinerario5`, `itinerario6`, `itinerario7`, `itinerario8`, `tarifas`, `tarifas2`, `tarifas3`, `tarifas4`, `tarifas5`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                   (generated_id, product.destino, product.subtitulo, product.date, product.date2, product.date3, product.days, product.nights, product.regimen, product.transporte, product.periodo, product.paquete, product.descripcion, product.moneda, product.precio, product.adicional, product.image, product.desde, product.hotel, product.incluye, product.incluye2, product.incluye3, product.incluye4, product.observaciones, product.observaciones2, product.observaciones3, product.itinerario, product.itinerario2, product.itinerario3, product.itinerario4, product.itinerario5, product.itinerario6, product.itinerario7, product.itinerario8, product.tarifas, product.tarifas2, product.tarifas3, product.tarifas4, product.tarifas5))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Product created successfully, ID: " + generated_id}

# Modificar producto
@router.put('/products/{id}')

def modProduct(id: str, product: Product):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("UPDATE `Products` SET destino = %s, subtitulo = %s, date = %s, date2 = %s, date3 = %s, days = %s, nights = %s, regimen = %s, transporte = %s, periodo = %s, paquete = %s, descripcion = %s, moneda = %s, precio = %s, adicional = %s, image = %s, desde = %s, hotel = %s, incluye = %s, incluye2 = %s, incluye3 = %s, incluye4 = %s, observaciones = %s, observaciones2 = %s, observaciones3 = %s, itinerario = %s, itinerario2 = %s, itinerario3 = %s, itinerario4 = %s, itinerario5 = %s, itinerario6 = %s, itinerario7 = %s, itinerario8 = %s, tarifas = %s, tarifas2 = %s, tarifas3 = %s, tarifas4 = %s, tarifas5 = %s WHERE id = %s", (product.destino, product.subtitulo, product.date, product.date2, product.date3, product.days, product.nights, product.regimen, product.transporte, product.periodo, product.paquete, product.descripcion, product.moneda, product.precio, product.adicional, product.image, product.desde, product.hotel, product.incluye, product.incluye2, product.incluye3, product.incluye4, product.observaciones, product.observaciones2, product.observaciones3, product.itinerario, product.itinerario2, product.itinerario3, product.itinerario4, product.itinerario5, product.itinerario6, product.itinerario7, product.itinerario8, product.tarifas, product.tarifas2, product.tarifas3, product.tarifas4, product.tarifas5, id))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Product updated successfully"}

# Eliminar producto
@router.delete('/products/{id}')

def delProducts(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM `Products` WHERE id = %s", (id,))

    connection.commit()

    cursor.close()

    connection.close()
    return {"message": "Product deleted successfully"}