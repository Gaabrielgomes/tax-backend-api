from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    cnpj: Mapped[str] = mapped_column(
        String(14),
        unique=True,
        index=True,
        nullable=False
    )