from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Literal, Optional


class UserCreate(BaseModel):
    email: EmailStr
    password:str

class User(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    

class UserLogin(BaseModel):
    email: EmailStr
    password:str

#using pydantic to see if data coming to api is correct and structured
class PostBase(BaseModel):
    title:  str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass
#pydantic for response of created and updated post
class Post(PostBase):
    created_at:datetime
    id:int
    owner_id:int
    owner: User

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        from_attributes=True
    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id:Optional[int]=None

class Vote(BaseModel):
    post_id:int
    dir:Literal[0,1]