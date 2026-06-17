from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class Telemetria(Base):
    __tablename__ = 'telemetria'
    
    id = Column(Integer, primary_key=True, index=True)
    ip_origem = Column(String)
    porta_origem = Column(Integer)
    timestamp = Column(String, index=True)
    profundidade = Column(Float)
    temperatura = Column(Float)
    pressao = Column(Float)
    