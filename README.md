1. To populate database: python manage.py populate_data

2. To access apis we need a token:

url : https://herokudrfapp.herokuapp.com/api/token/
method : POST
data : {
    "username": "kailash@xyz.com",
    "password": "welcome@123"
}

3. To get data:

url: https://herokudrfapp.herokuapp.com/getdata/
method: GET
Add token to Authorization (Type 'Bearer Token')

4. Refresh token can be used to get new token against expired access-token

url : https://herokudrfapp.herokuapp.com/api/refresh/
methed: POST
data : {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJleHAiOjE2MDM2MjUxMTAsImp0aSI6ImMxY2I4NDBiMDk0ZDQyYzk5M2Q5Y2Q0MzI2NmZkMGQ1IiwidG9rZW5fdHlwZSI6InJlZnJlc2gifQ.YznA9-cfIuZTH95QJ0k6kf7yjtowOdNplkrWV2ss1e4"
}
