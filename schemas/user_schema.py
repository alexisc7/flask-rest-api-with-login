# schemas/user_schema.py
from __future__ import annotations
from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, Field, model_validator

class UserBase(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=50)]
    email: EmailStr

class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=6)]

class UserUpdate(BaseModel):
    username: Optional[Annotated[str, Field(min_length=3, max_length=50)]]
    email:    Optional[EmailStr]
    password: Optional[Annotated[str, Field(min_length=6)]]

    @model_validator(mode='before')
    def at_least_one_field(cls, values):
        # 'values' es el dict crudo: verificamos que al menos haya un valor no nulo
        if not any(values.values()):
            raise ValueError("Proporcioná al menos un campo a actualizar")
        return values