from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave_secreta"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30

def crear_token(sub: str, es_admin: bool):
  expire = datetime.now(datetime.timezone.utc) + timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
  data = {
    "sub": sub,
    "exp": expire,
    "es_admin": es_admin
  }

  token =jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

  return token

def verificar_token(token: str):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
  
  except JWTError:
    return None