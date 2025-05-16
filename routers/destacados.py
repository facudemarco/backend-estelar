from fastapi import APIRouter, HTTPException
from models.product import Destacados
from sqlalchemy import text
from Database.dbGetConnection import engine
import uuid

router = APIRouter()

# Get all features
@router.get('/destacados')
def getFeatures():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM destacados"))
            features = result.mappings().all()
            return features
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Filter features by id
@router.get('/destacados/{id}')
def getFeaturesById(id: str):
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM destacados WHERE ID = :id"),
                {"id": id}
            )
            feature = result.mappings().first()
            if feature is None:
                raise HTTPException(status_code=404, detail="Feature not found.")
            return feature
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create feature
@router.post('/create_feature')
def createFeature(features: Destacados):
    generated_id = str(uuid.uuid4())

    query = text("""
        INSERT INTO destacados (ID, image)
        VALUES (:ID, :image)
    """)

    try:
        with engine.begin() as conn:
            conn.execute(query, {
                "ID": generated_id,
                "image": features.image
            })
        return {"message": f"Feature created successfully, ID: {generated_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Modify feature
@router.put('/features/{id}')
def modFeature(id: str, features: Destacados):
    query = text("""
        UPDATE destacados SET image = :image WHERE ID = :id
    """)

    try:
        with engine.begin() as conn:
            result = conn.execute(query, {
                "id": id,
                "image": features.image
            })
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="Feature not found.")
        return {"message": "Feature updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete feature
@router.delete('/features/{id}')
def delFeatures(id: str):
    try:
        with engine.begin() as conn:
            result = conn.execute(text("DELETE FROM destacados WHERE ID = :id"), {"id": id})
            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="Feature not found.")
        return {"message": "Feature deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))