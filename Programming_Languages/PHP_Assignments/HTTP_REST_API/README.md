# HTTP REST API using PHP

A simple REST API developed using PHP to demonstrate how HTTP methods work, how to read request headers and JSON request bodies, and how to return structured JSON responses with appropriate HTTP status codes.

Overview

This project demonstrates the fundamentals of building a RESTful API using PHP. It supports HTTP request methods such as GET, POST, PUT, and DELETE, with JSON-based communication between the client and server.

A simple HTML and JavaScript interface is also included to test API requests without requiring external API testing tools.

## Features

- GET: Retrieve data and display request headers.

- POST: Receive JSON data and simulate creating a resource.

- PUT: Receive JSON data and simulate updating a resource.

- DELETE: Simulate deleting a resource.

- JSON Handling: Read and decode JSON request bodies.

- Request Headers: Read HTTP request headers using PHP.

- Error Handling: Detect invalid JSON and return an appropriate error response.

- HTTP Status Codes: Return suitable status codes for different operations.

- Method Validation: Reject unsupported HTTP methods.

## Technologies Used

- PHP

- HTML5

- CSS3

- JavaScript

- Fetch API

- JSON

- Apache Server (XAMPP)

## Project Structure

```bash
HTTP_REST_API/
│
├── index.php
├── page.html
├── README.md
│
└── screenshots/
    ├── api-get.png
    ├── api-post.png
    ├── api-put.png
    ├── api-delete.png
    └── api-error.png
```


## Installation and Setup

**1. Requirements**

- Windows OS

- XAMPP

- PHP

- Apache Web Server

- Web Browser

**2. Configure Apache**

Make sure Apache is configured to access your project directory.

**3. Start Apache**

Open XAMPP Control Panel and start the Apache service.

**4. Access the Project**

Open the following URL in your browser:

```bash
http://localhost/PHP_Assignments/HTTP_REST_API/page.html
```

## API Endpoints

| Method | Endpoint  |  Description |
| GET   |  /index.php | Retrieve request information |

POST

/index.php

Receive data

PUT

/index.php

Update data (simulated)

DELETE

/index.php

Delete data (simulated)

HTTP Status Codes

Status Code

Description

200 OK

Request processed successfully

201 Created

Resource creation simulated successfully

400 Bad Request

Invalid JSON format

405 Method Not Allowed

Unsupported HTTP method

Testing the API

The project includes a simple web-based testing interface.

Open test.html in your browser through the local Apache server.

Enter JSON data in the request body field.

Select an HTTP method.

Click the corresponding button.

View the HTTP status code and JSON response.

Example JSON Request