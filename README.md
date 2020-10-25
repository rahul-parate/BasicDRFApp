1. To populate database: python manage.py populate_data

2. To access apis we need a token:

url : localhost:8000/api/token/
method : POST
data : {
    "username": "kailash@xyz.com",
    "password": "welcome@123"
}

3. To get data:

url: localhost:8000/getdata/
method: GET
Add token to Authorization (Type 'Bearer Token')
