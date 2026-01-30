from datetime import date
from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    username: str = Field(min_length=4)
    password: str = Field(min_length=8)
    role: str


class BeneficiaryCreate(BaseModel):
    code: str = Field(min_length=10)
    apellido_paterno: str
    apellido_materno: str
    nombres: str
    celular: str | None = None
    direccion: str | None = None
    observaciones: str | None = None


class BeneficiaryResponse(BeneficiaryCreate):
    id: int

    class Config:
        from_attributes = True


class CreditCreate(BaseModel):
    beneficiary_id: int
    credit_code: str
    monto: float
    interes: float
    fecha_credito: date
    fecha_limite: date


class CreditResponse(CreditCreate):
    id: int
    estado: str

    class Config:
        from_attributes = True


class PaymentCreate(BaseModel):
    credit_id: int
    fecha_pago: date
    capital: float
    interes: float
    otros: float = 0
    tipo_pago: str


class PaymentResponse(PaymentCreate):
    id: int

    class Config:
        from_attributes = True
