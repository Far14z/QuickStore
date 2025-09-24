from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

"""
Hashes a plain password and returns the hashed password.
"""
def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

"""
Verifies a plain password and a hashed password.
"""
def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
