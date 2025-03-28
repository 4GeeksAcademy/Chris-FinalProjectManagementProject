from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Freelancer(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

class Client(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Project_Manger(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Project(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    project_manager: Mapped[str] = mapped_column(String(120),nullable=False)
    client: Mapped[str] = mapped_column(String(120), nullable=False)
    budget: Mapped[float] = mapped_column(nullable=False)
    freelancers: Mapped[str] = mapped_column(String(120),nullable=False)
    tasks: Mapped[str] = mapped_column(String(120),nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
           
        }
        

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120),nullable=False)
    description: Mapped[str] = mapped_column(String(120),nullable=False)
    progress: Mapped[str] = mapped_column(String(120),nullable=False)
    project_id: Mapped[str] = mapped_column(String(120),nullable=False)
    assignee: Mapped[str] = mapped_column(String(120),nullable=False)
    due_date: Mapped[str] = mapped_column(String(120),nullable=False)
    cost: Mapped[str] = mapped_column(String(120),nullable=False)
    
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }