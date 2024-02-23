from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///your_database.db', echo=True)

Base = declarative_base()

student_subject = Table('student_subject', Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id')),
    Column('subject_id', Integer, ForeignKey('subject.id'))
)

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    subjects = relationship("Subject", secondary=student_subject, back_populates="students")

class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", secondary=student_subject, back_populates="subjects")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

student1 = Student(name="John")
student2 = Student(name="Alice")

english_subject = Subject(name="English")
math_subject = Subject(name="Math")

student1.subjects.append(english_subject)
student1.subjects.append(math_subject)
student2.subjects.append(english_subject)

session.add_all([student1, student2, english_subject, math_subject])
session.commit()

english_students = session.query(Student).join(Student.subjects).filter(Subject.name == 'English').all()

for student in english_students:
    print(student.name)
