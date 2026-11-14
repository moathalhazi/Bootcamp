<?php

require_once 'config/session.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: index.php');
    exit;
}

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

// Demonstration credentials only
if ($username === 'admin' && $password === 'Admin@123') {

    // Regenerate session ID after authentication
    session_regenerate_id(true);

    $_SESSION['authenticated'] = true;
    $_SESSION['username'] = $username;

    $_SESSION['login_time'] = date('Y-m-d H:i:s');

    header('Location: dashboard.php');
    exit;

} else {

    echo "Invalid username or password.";

}