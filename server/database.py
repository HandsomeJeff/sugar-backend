from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_url = "sqlite:///./data.db"

engine = create_engine(sqlalchemy_url,
                       connext_args={
                           "check_same_thread": False
                       })

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


