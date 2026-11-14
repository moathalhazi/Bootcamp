<?php

require_once 'config/session.php';

if (!isset($_SESSION['authenticated'])) {
    header('Location: index.php');
    exit;
}

?>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <title>Secure Dashboard</title>

    <link rel="stylesheet" href="assets/style.css">

</head>

<body>

<div class="container">

    <h1>Secure Dashboard</h1>

    <h2>
        Welcome,
        <?= htmlspecialchars($_SESSION['username']) ?>
    </h2>

    <div class="info">

        <p>
            Session ID:
            <strong><?= htmlspecialchars(session_id()) ?></strong>
        </p>

        <p>
            Login Time:
            <?= htmlspecialchars($_SESSION['login_time']) ?>
        </p>

        <p class="success">
            Your session is protected!
        </p>

    </div>

    <a href="cookie_test.php">
        <button>Test Cookie Security</button>
    </a>

    <a href="logout.php">
        <button class="danger">Logout</button>
    </a>

</div>

</body>
</html>