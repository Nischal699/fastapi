from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        """Hash a password using bcrypt."""
        hashed_password = pwd_cxt.hash(password)
        
        return hashed_password
    
    def verify(hashed_password: str, plain_password: str):
        """Verify a password against a hashed password."""
        return pwd_cxt.verify(plain_password, hashed_password)