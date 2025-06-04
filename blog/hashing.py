from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        """Hash a password using bcrypt."""
        hashed_password = pwd_cxt.hash(password)
        
        return hashed_password