<?php

require_once 'config/session.php';

// Detect HTTPS
$isSecure = (
    !empty($_SERVER['HTTPS']) &&
    $_SERVER['HTTPS'] !== 'off'
);

// Create an unprotected cookie
setcookie('unprotected_cookie', 'SensitiveData123', [
    'expires' => time() + 3600,
    'path' => '/',
    'httponly' => false,
    'secure' => $isSecure,
    'samesite' => 'Lax'
]);

// Create a protected cookie
setcookie('protected_cookie', 'ProtectedData456', [
    'expires' => time() + 3600,
    'path' => '/',
    'httponly' => true,
    'secure' => $isSecure,
    'samesite' => 'Strict'
]);

?>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <title>Cookie Security Test</title>

    <link rel="stylesheet" href="assets/style.css">

</head>

<body>

<div class="container">

    <h1>Cookie Security Test</h1>

    <div class="info">

        <h3>Unprotected Cookie</h3>

        <p>HttpOnly: Disabled</p>

        <p id="unprotected">Checking...</p>

    </div>

    <div class="info">

        <h3>Protected Cookie</h3>

        <p>HttpOnly: Enabled</p>

        <p id="protected">Checking...</p>

    </div>

    <button onclick="testCookies()">
        Run JavaScript Test
    </button>

    <a href="dashboard.php">
        <button>Back to Dashboard</button>
    </a>

</div>

<script src="assets/script.js"></script>

</body>
</html>