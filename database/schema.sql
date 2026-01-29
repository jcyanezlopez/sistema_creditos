-- Esquema base compatible con PostgreSQL/MySQL

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE beneficiaries (
  id SERIAL PRIMARY KEY,
  code VARCHAR(20) UNIQUE NOT NULL,
  apellido_paterno VARCHAR(80) NOT NULL,
  apellido_materno VARCHAR(80) NOT NULL,
  nombres VARCHAR(120) NOT NULL,
  celular VARCHAR(30),
  direccion VARCHAR(255),
  observaciones TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE credits (
  id SERIAL PRIMARY KEY,
  beneficiary_id INTEGER NOT NULL REFERENCES beneficiaries(id),
  credit_code VARCHAR(30) UNIQUE NOT NULL,
  monto NUMERIC(12,2) NOT NULL,
  interes NUMERIC(6,2) NOT NULL,
  fecha_credito DATE NOT NULL,
  fecha_limite DATE NOT NULL,
  estado VARCHAR(20) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE payment_schedules (
  id SERIAL PRIMARY KEY,
  credit_id INTEGER NOT NULL REFERENCES credits(id),
  cuota_numero INTEGER NOT NULL,
  fecha_vencimiento DATE NOT NULL,
  capital NUMERIC(12,2) NOT NULL,
  interes NUMERIC(12,2) NOT NULL,
  otros NUMERIC(12,2) NOT NULL DEFAULT 0,
  saldo NUMERIC(12,2) NOT NULL,
  estado VARCHAR(20) NOT NULL
);

CREATE TABLE payments (
  id SERIAL PRIMARY KEY,
  credit_id INTEGER NOT NULL REFERENCES credits(id),
  fecha_pago DATE NOT NULL,
  capital NUMERIC(12,2) NOT NULL,
  interes NUMERIC(12,2) NOT NULL,
  otros NUMERIC(12,2) NOT NULL DEFAULT 0,
  tipo_pago VARCHAR(20) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE refinancings (
  id SERIAL PRIMARY KEY,
  credit_id INTEGER NOT NULL REFERENCES credits(id),
  monto_adicional NUMERIC(12,2) NOT NULL,
  interes NUMERIC(6,2) NOT NULL,
  estado VARCHAR(20) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE amortizations (
  id SERIAL PRIMARY KEY,
  credit_id INTEGER NOT NULL REFERENCES credits(id),
  monto NUMERIC(12,2) NOT NULL,
  fecha DATE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  accion VARCHAR(120) NOT NULL,
  entidad VARCHAR(120) NOT NULL,
  entidad_id INTEGER NOT NULL,
  detalle TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
