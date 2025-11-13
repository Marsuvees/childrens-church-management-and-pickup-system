from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, Date
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os
from urllib import parse
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create a SQLAlchemy engine and session
try:
    username = "marsuvees"
    password = parse.quote(os.environ.get('MARSUVEES_PSQL_PASS'))
    host = "localhost"
    port = 5432
    database = "rent_reminder_system"
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')  # Use your desired database connection URL
except:
    print('Dropping to SQLite')
    engine = create_engine('sqlite:///ccm_system.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

class Family(Base):
    __tablename__ = 'family'
    id = Column(Integer, primary_key=True)
    reg_date = Column(Date, nullable=False)

class Guardian(Base):
    __tablename__ = 'guardians'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    family_id = Column(Integer, ForeignKey('family.id'))

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date, nullable=False)
    family_id = Column(Integer, ForeignKey('family.id'))
    
class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    class_code = Column(String, nullable=True)

class Logs(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('children.id'))
    event = Column(String, nullable=False)
    signed_in_by = Column(String, nullable=False)
    signed_out_by = Column(String, nullable=False)
    sign_out_time = Column(DateTime, nullable=True)
    
class Roster(Base):
    __tablename__ = 'roster'
    id = Column(Integer, primary_key=True)
    staff = Column(Integer, ForeignKey('staff.id'))
    topic = Column(String, nullable=True)
    date = Column(Date, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    from bcrypt import hashpw, gensalt
    salt = gensalt()

    # Create a default admin user

    admin_1 = Admin(username='admin1', password=hashpw('password123'.encode('utf-8'), salt).decode('utf-8'))

    session.add(admin_1)
    session.commit()
    session.close()