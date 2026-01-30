<?php
?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sistema de Créditos - Login</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f5f7fb; display: flex; justify-content: center; align-items: center; height: 100vh; }
    .card { background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); width: 360px; }
    label { display: block; margin-top: 1rem; font-weight: 600; }
    input { width: 100%; padding: 0.6rem; margin-top: 0.4rem; border-radius: 8px; border: 1px solid #cbd5e1; }
    button { margin-top: 1.5rem; width: 100%; padding: 0.75rem; background: #1d4ed8; color: #fff; border: none; border-radius: 8px; font-weight: 600; }
    .note { margin-top: 1rem; font-size: 0.85rem; color: #64748b; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Ingreso al sistema</h2>
    <form method="post" action="/login.php">
      <label for="username">Usuario</label>
      <input id="username" name="username" type="text" required />

      <label for="password">Contraseña</label>
      <input id="password" name="password" type="password" required />

      <button type="submit">Ingresar</button>
    </form>
    <p class="note">Conecte este formulario con el API FastAPI para autenticar.</p>
  </div>
</body>
</html>
