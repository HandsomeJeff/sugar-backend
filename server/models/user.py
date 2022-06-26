from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from server.database import Base

class User(Base):
    __tablename__ = "users"

    address = Column(String, primary_key=True, index=True)
    
