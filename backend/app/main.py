from fastapi import FastAPI

from app.config.database import Base
from app.config.database import engine

from app.routes.employeeRoutes import router as employee_router


Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(employee_router)

