from pydantic import BaseModel

class TelemetriaCreate(BaseModel):
    ip_origem: str
    porta_origem: int
    timestamp: str
    profundidade: float
    temperatura: float
    pressao: float
# Modelo de resposta para a API, removendo informações sensíveis
class TelemetriaResponse(BaseModel):
    id: int
    timestamp: str
    profundidade: float
    temperatura: float
    pressao: float
    class Config:
        from_attributes = True
