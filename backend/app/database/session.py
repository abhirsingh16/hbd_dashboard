from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from fastapi import Depends


DATABASE_URL = "mysql+pymysql://root:12345@localhost/hbd"


engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)


def get_db_session():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()    
    finally:
        db.close()


SessionDep = Depends(get_db_session)  # Create a dependency for DB session
