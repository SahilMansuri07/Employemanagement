from pydantic import BaseModel, EmailStr


class CreateEmployee(BaseModel):
    name: str
    email: EmailStr
    department: str