# 📦 Product Data Service API  
Product Data Service API is a **FastAPI** application designed to fetch product data, SKUs, and prices. The API allows filtering data based on **product models**, **SKUs**, **price groups**, **price types**, and **date ranges**.  

It uses Basic Authentication, so users must log in with a username and password:

Test Users:
admin / admin123

The API can be tested using cURL, Postman, or any HTTP client.


# 📡 Testing API Endpoints

**Home Route**
- Endpoint: GET /
- cURL Command:   curl -u mladen:1234 "http://127.0.0.1:8000/model?entityId=6479208"
