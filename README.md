# Sistema de Créditos

Plataforma para gestión de créditos con perfiles **Elaborador** y **Aprobador**, con módulos de beneficiarios, créditos, pagos, reportes y auditoría. El stack recomendado combina:

- **Backend**: Python + FastAPI (API REST, lógica de negocio y seguridad).
- **Frontend**: PHP (panel administrativo, formularios y reportes).
- **Base de datos**: PostgreSQL o MySQL.

## Objetivos funcionales

- Autenticación segura (JWT + hash de contraseñas).
- Roles: **Elaborador** (crea y edita borradores) y **Aprobador** (aprueba créditos, refinanciamientos y amortizaciones).
- Beneficiarios con código alfanumérico de 10+ caracteres.
- Créditos con sufijo en el código (por ejemplo `CF` o iniciales) y estado `ELABORADO`/`APROBADO`.
- Plan de pagos generado al aprobar; pagos individuales y masivos (Excel).
- Refinanciar, amortizar y liquidar con recalculo de intereses.
- Reportes por rango de fechas, estado y orden alfabético.
- Auditoría de acciones relevantes.

## Estructura

- `backend/`: API FastAPI.
- `frontend-php/`: UI administrativa en PHP (formulario base).
- `database/`: esquema SQL con entidades principales.
- `docs/`: reglas de negocio y reportes.

## Puesta en marcha (backend)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Puesta en marcha (frontend PHP)

```bash
cd frontend-php/public
php -S localhost:8080
```

## Base de datos

El esquema de referencia está en `database/schema.sql` y puede adaptarse a PostgreSQL o MySQL.
