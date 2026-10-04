from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.config.database import Base


class Employee(Base):

    __tablename__ = "tbl_employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True)

    department = Column(String(100))