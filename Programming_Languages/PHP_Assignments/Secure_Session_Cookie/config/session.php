<?php

// Prevent direct access to this configuration
if (session_status() === PHP_SESSION_NONE) {

    // Detect HTTPS connection
    $isSecure = (
        !empty($_SERVER['HTTPS']) &&
        $_SERVER['HTTPS'] !== 'off'
    );

    // Security configuration
    ini_set('session.use_strict_mode', '1');
    ini_set('session.use_only_cookies', '1');
    ini_set('session.use_trans_sid', '0');

    // Configure session cookie
    session_set_cookie_params([
        'lifetime' => 0,
        'path' => '/',
        'domain' => '',
        'secure' => $isSecure,
        'httponly' => true,
        'samesite' => 'Strict'
    ]);

    // Start secure session
    session_start();
}