from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
  print(repr(password))
  print(len(password.encode("utf-8")))
  return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
  return pwd_context.verify(password, hashed)