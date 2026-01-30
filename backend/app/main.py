from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .db import SessionLocal, Base, engine
from . import schemas, crud, models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Créditos")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/beneficiarios", response_model=schemas.BeneficiaryResponse)
def create_beneficiary(payload: schemas.BeneficiaryCreate, db: Session = Depends(get_db)):
    return crud.create_beneficiary(db, payload)


@app.get("/beneficiarios", response_model=list[schemas.BeneficiaryResponse])
def list_beneficiaries(db: Session = Depends(get_db)):
    return crud.list_beneficiaries(db)


@app.post("/creditos", response_model=schemas.CreditResponse)
def create_credit(payload: schemas.CreditCreate, db: Session = Depends(get_db)):
    beneficiary = db.get(models.Beneficiary, payload.beneficiary_id)
    if not beneficiary:
        raise HTTPException(status_code=404, detail="Beneficiario no encontrado")
    return crud.create_credit(db, payload)


@app.post("/creditos/{credit_id}/aprobar", response_model=schemas.CreditResponse)
def approve_credit(credit_id: int, db: Session = Depends(get_db)):
    credit = db.get(models.Credit, credit_id)
    if not credit:
        raise HTTPException(status_code=404, detail="Credito no encontrado")
    return crud.approve_credit(db, credit)


@app.post("/pagos", response_model=schemas.PaymentResponse)
def create_payment(payload: schemas.PaymentCreate, db: Session = Depends(get_db)):
    credit = db.get(models.Credit, payload.credit_id)
    if not credit:
        raise HTTPException(status_code=404, detail="Credito no encontrado")
    return crud.create_payment(db, payload)
