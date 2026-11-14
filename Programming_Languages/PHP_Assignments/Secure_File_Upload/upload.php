
<?php

// ==========================================
// 1. Security Configuration
// ==========================================

$uploadDirectory = __DIR__ . '/uploads/';

$maxFileSize = 5 * 1024 * 1024; // 5 MB

$allowedTypes = [
    'pdf'  => 'application/pdf',
    'png'  => 'image/png',
    'jpg'  => 'image/jpeg',
    'jpeg' => 'image/jpeg'
];

// ==========================================
// 2. Check Request Method
// ==========================================

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    exit("Error: Invalid request method.");
}

// ==========================================
// 3. Check Uploaded File
// ==========================================

if (!isset($_FILES['uploaded_file'])) {
    exit("Error: No file uploaded.");
}

$file = $_FILES['uploaded_file'];

// Check PHP upload errors

if ($file['error'] !== UPLOAD_ERR_OK) {
    exit("Error: File upload failed.");
}

// ==========================================
// 4. Validate File Size
// ==========================================

if ($file['size'] <= 0 || $file['size'] > $maxFileSize) {
    exit("Error: Invalid file size. Maximum allowed is 5 MB.");
}

// ==========================================
// 5. Validate File Extension
// ==========================================

$originalName = $file['name'];

$extension = strtolower(
    pathinfo($originalName, PATHINFO_EXTENSION)
);

if (!array_key_exists($extension, $allowedTypes)) {
    exit("Security Alert: File extension not allowed.");
}

// ==========================================
// 6. Validate Actual MIME Type
// ==========================================

$finfo = new finfo(FILEINFO_MIME_TYPE);

$mimeType = $finfo->file($file['tmp_name']);

if ($mimeType !== $allowedTypes[$extension]) {
    exit("Security Alert: MIME type mismatch.");
}

// ==========================================
// 7. Generate Random Secure Filename
// ==========================================

$randomName = bin2hex(random_bytes(16));

$newFileName = $randomName . '.' . $extension;

// ==========================================
// 8. Ensure Upload Directory Exists
// ==========================================

if (!is_dir($uploadDirectory)) {
    exit("Error: Upload directory does not exist.");
}

if (!is_writable($uploadDirectory)) {
    exit("Error: Upload directory is not writable.");
}

// ==========================================
// 9. Move Uploaded File
// ==========================================

$destination = $uploadDirectory . $newFileName;

if (move_uploaded_file($file['tmp_name'], $destination)) {

    // Restrict file permissions
    chmod($destination, 0640);

    echo "<h2>File Uploaded Successfully!</h2>";

    echo "<p>Generated Filename: " .
         htmlspecialchars($newFileName, ENT_QUOTES, 'UTF-8') .
         "</p>";

    echo "<p>MIME Type: " .
         htmlspecialchars($mimeType, ENT_QUOTES, 'UTF-8') .
         "</p>";

} else {

    exit("Error: Could not save uploaded file.");

}

?>
