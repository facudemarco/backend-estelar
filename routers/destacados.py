from fastapi import APIRouter, HTTPException
from models.product import Destacados
from Database.dbGetConnection import getConnection
import uuid

router = APIRouter()

# Get all features

@router.get('/destacados')

def getFeatures():
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `destacados`")

    products = cursor.fetchall()
    cursor.close()

    connection.close()
    return products

# Filter features by id

@router.get('/destacados/{id}')

def getFeaturesById(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `destacados` WHERE id = %s", (id,))

    product = cursor.fetchone()
    cursor.close()

    connection.close()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

# Create feature
@router.post('/create_feature')

def createFeature(features: Destacados):

    connection = getConnection()
    generated_id = str(uuid.uuid4())

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO `destacados`(`ID`, `image`) VALUES (%s, %s)", (generated_id, features.image))
    connection.commit()
    cursor.close()

    connection.close()

    return {"message": "Feature created successfully, ID: " + generated_id}

# Modify feature
@router.put('/features/{id}')

def modFeature(id: str, features: Destacados):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("UPDATE `destacados` SET image = %s WHERE id = %s", (features.image, id))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Feature updated successfully"}

# Delete feature
@router.delete('/features/{id}')

def delFeatures(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM `destacados` WHERE id = %s", (id,))

    connection.commit()

    cursor.close()

    connection.close()
    return {"message": "Feature deleted successfully"}