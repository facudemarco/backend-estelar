from fastapi import FastAPI, HTTPException, Request, APIRouter
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class FormData(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    email: str
    mensaje: str

def enviar_email(form_data: FormData):
    sender_email = "iweb.contacto@gmail.com"
    sender_password = os.environ.get("SENDER_PASSWORD")
    
    if not sender_password:
        raise HTTPException(status_code=500, detail="La contraseña del remitente no está configurada")
        
    receiver_email = "iweb.contacto@gmail.com"
    subject = f"Nuevo mensaje de contacto desde la Web de Estelar Viajes de {form_data.nombre}"
    body = f"Nombre: {form_data.nombre}\nApellido: {form_data.apellido}\nTeléfono: {form_data.telefono}\nEmail: {form_data.email}\nMensaje: {form_data.mensaje}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        raise HTTPException(status_code=500, detail="Error al enviar el correo")

@router.post("/send-email")
async def send_email(form_data: FormData):
    enviar_email(form_data)
    return {"message": "Formulario enviado exitosamente"}
