from fastapi import APIRouter , Depends, status, HTTPException , Response
from sqlalchemy.orm import Session
from .. import schemas, models ,database
from typing import List
from ..hashing import Hash
from ..repository import user 

router = APIRouter(
    prefix="/User",  # You can set a prefix for all routes in this router
    tags=["Users"]  # Tags for documentation purposes
)

get_db = database.get_db


@router.post('/',response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)