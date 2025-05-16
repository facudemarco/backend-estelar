from fastapi import APIRouter, HTTPException
from models.product import Cartelera
from sqlalchemy import text
from Database.dbGetConnection import engine
import uuid

router = APIRouter()

# 🔹 Get all flyers
@router.get('/cartelera')
def getFeatures():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM cartelera"))
            rows = result.mappings().all()
            return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔹 Filter flyers by ID
@router.get('/cartelera/{id}')
def getFlyersById(id: str):
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM cartelera WHERE ID = :id"),
                {"id": id}
            )
            row = result.mappings().first()
            if row is None:
                raise HTTPException(status_code=404, detail="Flyer not found.")
            return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔹 Create flyer
@router.post('/create_flyer')
def createFlyer(flyers: Cartelera):
    generated_id = str(uuid.uuid4())

    query = text("""
        INSERT INTO cartelera (ID, image, descripcion, periodo)
        VALUES (:ID, :image, :descripcion, :periodo)
    """)

    try:
        with engine.begin() as conn:
            conn.execute(query, {
                "ID": generated_id,
                "image": flyers.image,
                "descripcion": flyers.descripcion,
                "periodo": flyers.periodo
            })
        return {"message": f"Flyer created successfully, ID: {generated_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔹 Modify flyer
@router.put('/flyers/{id}')
def modFlyer(id: str, flyers: Cartelera):
    query = text("""
        UPDATE cartelera
        SET image = :image,
            descripcion = :descripcion,
            periodo = :periodo
        WHERE ID = :id
    """)

    try:
        with engine.begin() as conn:
            result = conn.execute(query, {
                "id": id,
                "image": flyers.image,
                "descripcion": flyers.descripcion,
                "periodo": flyers.periodo
            })

            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="Flyer not found.")
        return {"message": "Flyer updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 🔹 Delete flyer
@router.delete('/flyers/{id}')
def delFlyer(id: str):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("DELETE FROM cartelera WHERE ID = :id"),
                {"id": id}
            )

            if result.rowcount == 0:
                raise HTTPException(status_code=404, detail="Flyer not found.")
        return {"message": "Flyer deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))