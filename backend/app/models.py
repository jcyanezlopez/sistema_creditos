from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, Date, Enum, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum("ELABORADOR", "APROBADOR", name="user_roles"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Beneficiary(Base):
    __tablename__ = "beneficiaries"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)
    apellido_paterno = Column(String(80), nullable=False)
    apellido_materno = Column(String(80), nullable=False)
    nombres = Column(String(120), nullable=False)
    celular = Column(String(30), nullable=True)
    direccion = Column(String(255), nullable=True)
    observaciones = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    credits = relationship("Credit", back_populates="beneficiary")


class Credit(Base):
    __tablename__ = "credits"

    id = Column(Integer, primary_key=True, index=True)
    beneficiary_id = Column(Integer, ForeignKey("beneficiaries.id"), nullable=False)
    credit_code = Column(String(30), unique=True, nullable=False, index=True)
    monto = Column(Numeric(12, 2), nullable=False)
    interes = Column(Numeric(6, 2), nullable=False)
    fecha_credito = Column(Date, nullable=False)
    fecha_limite = Column(Date, nullable=False)
    estado = Column(Enum("ELABORADO", "APROBADO", name="credit_status"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    beneficiary = relationship("Beneficiary", back_populates="credits")
    payments = relationship("Payment", back_populates="credit")
    schedules = relationship("PaymentSchedule", back_populates="credit")


class PaymentSchedule(Base):
    __tablename__ = "payment_schedules"

    id = Column(Integer, primary_key=True, index=True)
    credit_id = Column(Integer, ForeignKey("credits.id"), nullable=False)
    cuota_numero = Column(Integer, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    capital = Column(Numeric(12, 2), nullable=False)
    interes = Column(Numeric(12, 2), nullable=False)
    otros = Column(Numeric(12, 2), nullable=False, default=0)
    saldo = Column(Numeric(12, 2), nullable=False)
    estado = Column(Enum("PENDIENTE", "PAGADO", name="schedule_status"), nullable=False)

    credit = relationship("Credit", back_populates="schedules")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    credit_id = Column(Integer, ForeignKey("credits.id"), nullable=False)
    fecha_pago = Column(Date, nullable=False)
    capital = Column(Numeric(12, 2), nullable=False)
    interes = Column(Numeric(12, 2), nullable=False)
    otros = Column(Numeric(12, 2), nullable=False, default=0)
    tipo_pago = Column(Enum("INDIVIDUAL", "MASIVO", name="payment_type"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    credit = relationship("Credit", back_populates="payments")


class Refinancing(Base):
    __tablename__ = "refinancings"

    id = Column(Integer, primary_key=True, index=True)
    credit_id = Column(Integer, ForeignKey("credits.id"), nullable=False)
    monto_adicional = Column(Numeric(12, 2), nullable=False)
    interes = Column(Numeric(6, 2), nullable=False)
    estado = Column(Enum("ELABORADO", "APROBADO", name="refi_status"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Amortization(Base):
    __tablename__ = "amortizations"

    id = Column(Integer, primary_key=True, index=True)
    credit_id = Column(Integer, ForeignKey("credits.id"), nullable=False)
    monto = Column(Numeric(12, 2), nullable=False)
    fecha = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    accion = Column(String(120), nullable=False)
    entidad = Column(String(120), nullable=False)
    entidad_id = Column(Integer, nullable=False)
    detalle = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
