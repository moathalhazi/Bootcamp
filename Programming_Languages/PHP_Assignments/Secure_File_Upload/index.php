
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure File Upload</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #101827;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }

        .container {
            background: #1e293b;
            padding: 35px;
            border-radius: 15px;
            width: 90%;
            max-width: 450px;
            box-shadow: 0 10px 30px rgba(0,0,0,.3);
        }

        h1 {
            text-align: center;
            color: #38bdf8;
        }

        p {
            color: #cbd5e1;
            text-align: center;
        }

        input[type="file"] {
            width: 100%;
            margin: 25px 0;
            padding: 12px;
            background: #334155;
            border-radius: 8px;
            color: white;
        }

        button {
            width: 100%;
            padding: 13px;
            background: #0284c7;
            border: none;
            border-radius: 8px;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #0369a1;
        }

        .security {
            margin-top: 20px;
            font-size: 13px;
            line-height: 1.8;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Secure File Upload</h1>

    <p>Upload your files securely.</p>

    <form action="upload.php"
          method="POST"
          enctype="multipart/form-data">

        <input type="file"
               name="uploaded_file"
               accept=".pdf,.png,.jpg,.jpeg"
               required>

        <button type="submit">
            Upload File
        </button>

    </form>

    <div class="security">
        <strong>Security Features:</strong>
        <ul>
            <li>Maximum file size validation</li>
            <li>Extension whitelist</li>
            <li>MIME type verification</li>
            <li>Random filename generation</li>
            <li>Secure file storage</li>
        </ul>
    </div>

</div>

</body>
</html>
