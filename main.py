from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Telemetria
from schemas import TelemetriaCreate, TelemetriaResponse
from database import engine, get_db,Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/v1/telemetria", response_model=TelemetriaResponse)
def receber_dados(telemetria: TelemetriaCreate, db: Session = Depends(get_db)):
    try:
        # Criar uma nova instância do modelo Telemetria com os dados recebidos
        novo_registro = Telemetria( **telemetria.model_dump())
        
        # Adicionar a nova leitura ao banco de dados
        db.add(novo_registro)
        # Envia a nova leitura para o banco de dados
        db.commit()
        # Atualiza o objeto com o ID gerado pelo banco de dados
        db.refresh(novo_registro)  
        
        # Retornar a resposta com os dados da telemetria criada
        return novo_registro
    except Exception as e:
        # Em caso de erro, desfaz a transação e retorna um erro HTTP
        db.rollback()  
        raise HTTPException(status_code=500, detail=f"Erro ao processar os dados: {e}")