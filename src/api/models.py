from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


# project_freelancer = db.Table(
#     "project_freelancer",
#     db.Column("freelancer_id", db.ForeignKey("freelancer.id")),
#     db.Column("project_id", db.ForeignKey("project.id")),
# )


# class Freelancer(db.Model):
#     __tablename__ = "freelancer"
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     email: Mapped[str] = mapped_column(
#         String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(String(255), nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
#     first_name: Mapped[str] = mapped_column(String(50), nullable=False)
#     last_name: Mapped[str] = mapped_column(String(50), nullable=False)
#     skills: Mapped[str] = mapped_column(String(255), nullable=False)
#     phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
#     experience: Mapped[int] = mapped_column(Integer, nullable=False)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             "is_active": self.is_active,
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             "skills": self.skills,
#             "phone_number": self.phone_number,
#             "experience": self.experience,
#         }


class Client(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    about_me: Mapped[str] = mapped_column(String(2000), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "about_me": self.about_me,
        }



class ProjectManager(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    skills: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    experience: Mapped[str] = mapped_column(String(5000), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "skills": self.skills,
            "phone_number": self.phone_number,
            "experience": self.experience,
        }


class Project(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    project_manager: Mapped[str] = mapped_column(String(50), nullable=False)
    client: Mapped[str] = mapped_column(String(50), nullable=False)
    budget: Mapped[float] = mapped_column(Float, nullable=False)
    # freelancers: Mapped[str] = mapped_column(String(255), nullable=False)
    tasks: Mapped[str] = mapped_column(String(500), nullable=False)
    preferred_skills: Mapped[str] = mapped_column(String(500), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "project_manager": self.project_manager,
            "client": self.client,
            "budget": self.budget,
            # "freelancers": self.freelancers,
            "tasks": self.tasks,
            "preferred_skills": self.preferred_skills,
        }


class Invoice(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    invoice_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    date_issued: Mapped[str] = mapped_column(DateTime, nullable=False)
    date_due: Mapped[str] = mapped_column(DateTime, nullable=False)
    client: Mapped[str] = mapped_column(String(50), nullable=False)  # Client name
    project: Mapped[str] = mapped_column(String(120), nullable=False)  # Project name
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    tax_rate: Mapped[float] = mapped_column(Float, default=0.0)
    status: Mapped[str] = mapped_column(String(20), nullable=False)  # 'draft', 'sent', 'paid', 'overdue'
    notes: Mapped[str] = mapped_column(String(1000), nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "invoice_number": self.invoice_number,
            "date_issued": str(self.date_issued),
            "date_due": str(self.date_due),
            "client": self.client,
            "project": self.project,
            "amount": self.amount,
            "tax_rate": self.tax_rate,
            "status": self.status,
            "notes": self.notes,
        }


# class Task(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String(120), nullable=False)
#     description: Mapped[str] = mapped_column(String(255), nullable=False)
#     progress: Mapped[str] = mapped_column(String(50), nullable=False)
#     project_id: Mapped[int] = mapped_column(
#         Integer, db.ForeignKey("project.id"), nullable=False)
#     assignee_id: Mapped[int] = mapped_column(
#         Integer, db.ForeignKey("freelancer.id"), nullable=False)
#     due_date: Mapped[str] = mapped_column(DateTime, nullable=False)
#     cost: Mapped[float] = mapped_column(Float, nullable=False)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "progress": self.progress,
#             "project_id": self.project_id,
#             "assignee": self.assignee,
#             "due_date": str(self.due_date),
#             "cost": self.cost,
#         }

