#USUARIO MODEL: 
from pydantic import BaseModel


class Usuario(BaseModel):
    Documento: str
    Usuario:str
    Clave:str
    Nombre:str
    Apellido:str
    CorreoElectronico:str
    Direccion:str
    TarjetaCredito:float
    CVV:int
    
    