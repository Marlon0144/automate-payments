import pydantic
from pydantic import BaseModel

class TransactionBase(BaseModel):
    amount: float
    fee: float
    nameClient: str
    nameTutor: str

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    class Config:
        orm_mode = True