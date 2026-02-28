from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.client import ClientCreate, ClientResponse
from app.crud.client import create_client

router = APIRouter()


@router.post("/", response_model=ClientResponse)
def create_client_route(
    client: ClientCreate,
    db: Session = Depends(get_db)
):
    return create_client(db, client)