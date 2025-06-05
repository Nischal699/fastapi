from fastapi import APIRouter , Depends, status, HTTPException , Response
from sqlalchemy.orm import Session
from .. import schemas, models ,database , oauth2
from typing import List
from ..repository import blog

router = APIRouter(
    prefix="/Blog",  # You can set a prefix for all routes in this router
    tags=["Blogs"]  # Tags for documentation purposes
)

get_db = database.get_db

@router.get("/",response_model=list[schemas.ShowBlog], status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request : schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get("/{id}",status_code=200,response_model=schemas.ShowBlog)
def show(id: int,response: Response, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)