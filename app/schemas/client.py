from pydantic import BaseModel, field_validator


class ClientBase(BaseModel):
    name: str
    cnpj: str

    @field_validator("cnpj")
    @classmethod
    def validate_cnpj(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError("CNPJ must contain only digits")

        if len(value) != 14:
            raise ValueError("CNPJ must contain exactly 14 digits")

        return value


class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int

    model_config = {
        "from_attributes": True
    }