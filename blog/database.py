from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Use given url and force to communicate on the same thread
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create own db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Later we will inherit from this class to create each of the database models or classes
Base = declarative_base()

# Create connection with database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
