# Description
The present application is a simple Django Rest Framework Backend
for a notes application where there are the following functionalities.
<br>
To check the data stored in the database:
<br> After you create the superuser and have run all migrations,
you can check all the values stores by visiting 
http://localhost:8000/admin and logging in by the username and password
given during superuser creation.

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

# Steps to run
- Clone the repository
- Make the MYSQL database according to details in the `settings.py`
file under the following:
```python
# Connect to the Mysql DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'notes',
        'USER': 'notes_user',
        'PASSWORD': 'aahtheo@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Run: `pip install -r requirements.txt`
- Run: `python manage.py migrate`
- Create super user: `python manage.py createsuperuser`

# ToDo
- [ ] Correct the documentation by customizing for each view
