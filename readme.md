# User API Flask Application

This is a Flask application that provides REST API endpoints for CRUD (Create, Read, Update, and Delete) operations on a User resource. The application uses the PyMongo library to connect to a MongoDB database.

## Requirements

- Python 3.6 or higher
- Flask
- PyMongo

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/user-api.git
   ```

2. Navigate to the project directory:
    ```bash
    cd USER_API
    ```
3. Install the required dependencies:
    ```cmd
    pip install -r requirements.txt
    ```
4. Configure the MongoDB connection string in `config.py` . For example:
   
   ```python
   MONGO_URI = 'mongodb://localhost:27017/mydatabase'
   ```

## Usage
To start the Flask application, run the following command:

```bash
python app.py
```
This will satrt the application on  http://localhost:5000.

## REST API Endpoints
The following REST API endpoints are provided by the application:

- **GET /users** - Returns a list of all users.
- **GET /user/\<id>** - Returns the user with the specified ID.
- **POST /user** - Creates a new user with the specified data.
- **PUT /user/\<id>** - Updates the user with the specified ID with the new data.
- **DELETE /user/\<id>** - Deletes the user with the specified ID.

## Example Requests and Responses

### GET /users

Request
```bash
GET /users
```
Response

```json
[
    {
        "id": "1",
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "password1"
    },
    {
        "id": "2",
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "password": "password2"
    },
    ...
]

```

### GET /user/\<id>
Request

```bash
GET /users/1
```

Response

```json
{
    "id": "1",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "password1"
}
```

### POST /users
Request
```json
POST /users

{    
    "name": "Bob Smith",
    "email": "bob.smith@example.com",
    "password": "password3"
}
```

Response

```json
{
    "message": "User Created"
}
```

if `email` already exist

```json
{
    "error": "User already existes"
}
```

### PUT /users/\<id>

Request
```json
PUT /users/3

{
    "name": "Bobby Smith",
    "email": "bobby.smith@example.com",
    "password": "newpassword"
}
```

Response
```json
{"message": "user Updated"}
```

### DELETE /users/\<id>

Request
```bash
DELETE /users/3
```

Response
```json
{
    "message": "User with ID 3 has been deleted."
}
```

## Docker

This application can also be run as a Docker container. To build the Docker image, run the following command:

```bash
docker-compose up --build
```

