from pydoc import describe
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Product(BaseModel):
    id: Optional[str] = None
    destino: str
    subtitulo: str
    date: date
    date2: date
    days: str
    nights: str
    regimen: str
    transporte: str
    periodo: str
    paquete: str
    descripcion: str
    moneda: str
    precio: str
    adicional: str
    image: str
    desde: bool
    hotel: str
    incluye: str
    incluye2: str
    incluye3: str
    incluye4: str
    observaciones: str
    observaciones2: str
    observaciones3: str
    itinerario: str
    itinerario2: str
    itinerario3: str
    itinerario4: str
    itinerario5: str
    itinerario6: str
    itinerario7: str
    itinerario8: str
    tarifas: str
    tarifas2: str
    tarifas3: str
    tarifas4: str
    tarifas5: str
    
class Destacados(BaseModel):
    id: Optional[str] = None
    image: str
        
class Cartelera(BaseModel):
    id: Optional[str] = None
    image: str
    descripcion: str
    periodo: str