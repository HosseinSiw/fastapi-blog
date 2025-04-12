from fastapi import APIRouter, status, Depends, HTTPException, Query
from .dependencies import get_db, get_current_user
from models.posts import Post
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List
from models.user import User
from models.category import Category
from schemas.posts import (PostRetriveSchema,
                           PostCreationSchema,
                           PostUpdateSchema)
from typing import Optional


post_router = APIRouter(prefix='/posts', tags=['posts'])


# GET -- retrive all published posts, support both search and filter by category name.
@post_router.get('/', status_code=status.HTTP_200_OK, response_model=List[PostRetriveSchema])
def get_posts(db: Session = Depends(get_db),
    search: Optional[str] = Query(None, description="Search in title or content"),
    category: Optional[str] = Query(None, description="Filter Posts by their category"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),):
    
    query = db.query(Post).filter(Post.is_published==True)
    if search:
        query = query.filter(
            or_(
                Post.title.ilike(f"%{search}%"),
                Post.content.ilike(f"%{search}%")
            )
        )
    if category:
        category_obj = db.query(Category).filter(Category.name.ilike(category)).first()
        if not category_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"Error": "Category not found"})
    
        query = query.filter(Post.category_id==Category.id)

    posts = query.order_by(Post.created_at.desc()).offset(offset).limit(limit).all()
    count = query.count()
    return {
        "total count": count,
        "posts": posts
        }
    
# GET -- retrive a single post based on it id (primary key)
@post_router.get('/{post_id}/', status_code=200, response_model=PostRetriveSchema)
def get_single_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id==post_id).filter(Post.is_published==True).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    
    return post

# POST -- create a post
@post_router.post('/', response_model=PostRetriveSchema, status_code=status.HTTP_201_CREATED)
def create_post(post_data: PostCreationSchema, 
                db: Session=Depends(get_db), 
                current_user: User=Depends(get_current_user)):
    
    category_name = post_data.category_name.strip().lower()
    category = db.query(Category).filter(Category.name.ilike(category_name)).first()
    
    if not category:
        category = Category(name=category_name)
        db.add(category)
        db.commit()
        db.refresh(category)
        
    user_email = current_user['sub'].split(' ')[0]
    user = db.query(User).filter(User.email == user_email).first()
    new_post = Post(
            title=post_data.title,
            content=post_data.content,
            summary=post_data.summary,
            author_id=user.id,
            category_id=category.id
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(instance=new_post)
    return PostRetriveSchema(
    **new_post.__dict__,
    category_name=new_post.category.name
    )

# PATCH -- Update a post
@post_router.patch('/{post_id}/', response_model=PostRetriveSchema)
def update_post(post_id: int,
                post_data: PostUpdateSchema,
                db: Session=Depends(get_db), 
                current_user: User=Depends(get_current_user)):
    
    post = db.query(Post).filter(Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
    
    if not post.author_id == current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    
    if "category_name" in post_data.model_dump(exclude_unset=True):
        category = db.query(Category).filter(Category.name.ilike(post_data.category_name)).first()
        if not category:
            category = Category(name=post_data.category_name)
            db.add(category)
            db.commit()
            db.refresh(category)
        post.category_id = category.id
    
    for key, value in post_data.model_dump(exclude_unset=True).items():
        setattr(post, key, value)
    
    db.commit()
    db.refresh(post)
    return post

@post_router.delete("/{post_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail='Not allowed')
    
    db.delete(post)
    db.commit()
    return
