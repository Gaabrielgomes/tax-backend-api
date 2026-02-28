from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.client import Client
from app.schemas.client import ClientCreate


def get_client_by_cnpj(db: Session, cnpj: str):
    return db.query(Client).filter(Client.cnpj == cnpj).first()


def create_client(db: Session, client: ClientCreate):
    existing_client = get_client_by_cnpj(db, client.cnpj)

    if existing_client:
        raise HTTPException(
            status_code=400,
            detail="Client with this CNPJ already exists"
        )

    new_client = Client(**client.model_dump())

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client