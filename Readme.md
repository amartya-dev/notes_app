# Description
The present application is a simple Django Rest Framework Backend
for a notes application where there are the following functionalities

# Functionalities
- Add User (signup): <br> Make a `POST` request to 
http://localhost:8000/app/user with the following parameters as 
request body:<br>
```json
{
  "username": "string",
  "password": "string"
}
```
Response (on success):
```json
{
  "status": "account created"
}
```
Response (on failure):
```json
{
  "details": "<some error>"
}
```

- Add note (requires basic auth)<br>
Make a `POST` request to http://localhost:8000/app/sites/ with 
the following parameters:
```json
{
  "note": "string",
  "user_id": int
}
```
Response (on success):
```json
{
  "status": "success"
}
```

- View all notes for a given user: <br>
Make a `GET` request http://localhost:8000/app/sites/list/
?user_id=<user_id><br>

Response (on success):
```json
[
    {
        "user": "<username>",
        "note": "<note>"
    },
    {
        "user": "<username>",
        "note": "<note>"
    }
]
```
- Authenticate a user: <br>
Make a `POST` request to http://localhost:8000/app/user/auth with the 
following parameters:
```json
{
  "username": "string",
  "password": "string"
}
```
Response (on success):
```json
{
  "status": "success",
  "userId": int
}
```
Response (on failure):
```json
{
  "status": "access denied"
}
```
