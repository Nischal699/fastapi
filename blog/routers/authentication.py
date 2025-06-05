from fastapi import APIRouter ,Depends ,HTTPException, status
from ..import schemas, database , models
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    tags=["Authentication"]  # Tags for documentation purposes
)

@router.post("/login")
def login(request:schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    
    #generate a token or session here if needed
    return user    