from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import text
from app.config.database import get_db

from app.models.employeeModels import Employee

from app.utils.common import sendResponse

from app.schema.employeeSchemas import CreateEmployee

router = APIRouter(
    prefix="/employees",
)

@router.get("/list", summary="Get all employees", description="Fetches a list of all employees from the database.")
def get_all_employees(db: Session = Depends(get_db)):

    query = text("SELECT * FROM tbl_employees")

    result = db.execute(query)

    employees = result.mappings().all()

    return sendResponse(
        status_code=200,
        response_code=1,
        message="Employees fetched successfully",
        data=employees
    )


@router.post("/add", summary="Add a new employee", description="Adds a new employee to the database.")
def create_employee(
    employee: CreateEmployee,
    db: Session = Depends(get_db)
):
    try:
        query = text("SELECT * FROM tbl_employees WHERE email = :email")

        existing_employee = db.execute(query, {"email": employee.email}).mappings().first()

        if existing_employee:
            return sendResponse(
                status_code=400,
                response_code=1,
                message="Employee with this email already exists",
                data=None
            )

        query = text("""
            INSERT INTO tbl_employees
            (
                name,
                email,
                department
            )
            VALUES
            (
                :name,
                :email,
                :department
            )
        """)

        db.execute(
            query,
            {
                "name": employee.name,
                "email": employee.email,
                "department": employee.department
            }
        )
        db.commit()
        
        result = db.execute(text("SELECT LAST_INSERT_ID()"))

        employee_id = result.scalar()

        query = text("SELECT * FROM tbl_employees WHERE id = :id")

        employee = db.execute(query, {"id": employee_id}).mappings().first()

        return sendResponse(
            status_code=201,
            response_code=0,
            message="Employee created successfully",
            data=employee
        )

    except Exception as e:
        db.rollback()
        return sendResponse(
            status_code=500,
            response_code=1,
            message=str(e),
            data=None
        )
    
