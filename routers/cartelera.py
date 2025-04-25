from fastapi import APIRouter, HTTPException
from models.product import Cartelera
from Database.dbGetConnection import getConnection
import uuid

router = APIRouter()

# Get all flyers

@router.get('/cartelera')

def getFeatures():
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `cartelera`")

    products = cursor.fetchall()
    cursor.close()

    connection.close()
    return products

# Filter flyers by id

@router.get('/cartelera/{id}')

def getFlyersById(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `cartelera` WHERE id = %s", (id,))

    product = cursor.fetchone()
    cursor.close()

    connection.close()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

# Create flyer
@router.post('/create_flyer')

def createFlyer(flyers: Cartelera):

    connection = getConnection()
    generated_id = str(uuid.uuid4())

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO `cartelera`(`ID`, `image`, `descripcion`, `periodo`) VALUES (%s, %s, %s, %s)", (generated_id, flyers.image, flyers.descripcion, flyers.periodo))
    connection.commit()
    cursor.close()

    connection.close()

    return {"message": "Flyer created successfully, ID: " + generated_id}

# Modify flyer
@router.put('/flyers/{id}')

def modFlyer(id: str, flyers: Cartelera):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("UPDATE `cartelera` SET image = %s, descripcion = %s, periodo = %s WHERE id = %s", (flyers.image, flyers.descripcion, flyers.periodo, id))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Flyer updated successfully"}

# Delete flyer
@router.delete('/flyers/{id}')

def delFlyer(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM `cartelera` WHERE id = %s", (id,))

    connection.commit()

    cursor.close()

    connection.close()
    return {"message": "Flyer deleted successfully"}