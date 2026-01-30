from sqlalchemy.orm import Session

from . import models, schemas


def create_beneficiary(db: Session, data: schemas.BeneficiaryCreate) -> models.Beneficiary:
    beneficiary = models.Beneficiary(**data.model_dump())
    db.add(beneficiary)
    db.commit()
    db.refresh(beneficiary)
    return beneficiary


def list_beneficiaries(db: Session) -> list[models.Beneficiary]:
    return db.query(models.Beneficiary).order_by(models.Beneficiary.apellido_paterno).all()


def create_credit(db: Session, data: schemas.CreditCreate) -> models.Credit:
    credit = models.Credit(**data.model_dump(), estado="ELABORADO")
    db.add(credit)
    db.commit()
    db.refresh(credit)
    return credit


def approve_credit(db: Session, credit: models.Credit) -> models.Credit:
    credit.estado = "APROBADO"
    db.commit()
    db.refresh(credit)
    return credit


def create_payment(db: Session, data: schemas.PaymentCreate) -> models.Payment:
    payment = models.Payment(**data.model_dump())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment
