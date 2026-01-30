<?php
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: /');
    exit();
}

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';
?>
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Login procesado</title>
</head>
<body>
  <h2>Login recibido</h2>
  <p>Usuario: <?php echo htmlspecialchars($username); ?></p>
  <p>Este formulario debe integrarse con el endpoint de autenticación.</p>
</body>
</html>
