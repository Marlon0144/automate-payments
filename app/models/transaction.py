from sqlalchemy import Column, Integer, String, Float
from app.database import Base



class Transaction (Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Float, nullable=False, unique=False)
    fee = Column(Float, nullable=False, unique=False)
    name_client = Column(String, nullable=True, unique=False)
    name_tutor = Column(String, nullable=True, unique=False)