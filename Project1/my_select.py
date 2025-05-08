from sqlalchemy import func, desc
from config import Session
from models import Student, Grade, Subject, Group, Teacher

def select_1():
    with Session() as session:
        return session.query(
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        ).select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    with Session() as session:
        return session.query(
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        ).select_from(Grade).join(Student).join(Subject).filter(
            Subject.name == subject_name
        ).group_by(Student.id).order_by(desc('avg_grade')).limit(1).first()

def select_3(subject_name):
    with Session() as session:
        return session.query(
            Group.name,
            func.round(func.avg(Grade.grade), 2).label('avg_grade')
        ).select_from(Grade).join(Student).join(Group).join(Subject).filter(
            Subject.name == subject_name
        ).group_by(Group.id).all()

def select_4():
    with Session() as session:
        return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

def select_5(teacher_name):
    with Session() as session:
        return session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()

def select_6(group_name):
    with Session() as session:
        return session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    with Session() as session:
        return session.query(
            Student.fullname,
            Grade.grade
        ).select_from(Grade).join(Student).join(Group).join(Subject).filter(
            Group.name == group_name,
            Subject.name == subject_name
        ).all()

def select_8(teacher_name):
    with Session() as session:
        return session.query(
            func.round(func.avg(Grade.grade), 2)
        ).join(Subject).join(Teacher).filter(Teacher.fullname == teacher_name).scalar()

def select_9(student_name):
    with Session() as session:
        return session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).distinct().all()

def select_10(student_name, teacher_name):
    with Session() as session:
        return session.query(Subject.name).join(Grade).join(Student).join(Teacher).filter(
            Student.fullname == student_name,
            Subject.teacher.has(fullname=teacher_name)
        ).distinct().all()
