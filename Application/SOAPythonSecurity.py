#SOAPythonSecurity
from fastapi import FastAPI
from Core.Security.Decode.Base64Decode import base64Decode
from Core.Security.Encode.Base64Encode import base64Encode

app: FastAPI = FastAPI(title='SOAPythonSecurity',)

#Metodos

@app.get("/Base64Encode",summary="Base64 Encode", description="Cifrado Base 64",tags=["Base64"])
async def Base64Encode(plainText: str | None=None):
    Base64Encode = base64Encode()
    return None
@app.get("/Base64Decode",summary="Base64 Decode", description="Decifrado Base 64",tags=["Base64"])
async def Base64Decode(encodedText: str | None=None):
    Base64Decode = base64Decode()
    return None

