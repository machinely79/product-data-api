# 📦 Product Data Service API  

Product Data Service API is a **FastAPI** application designed to fetch product data, SKUs, and prices. The API allows filtering data based on **product models**, **SKUs**, **price groups**, **price types**, and **date ranges**.  

It uses Basic Authentication, so users must log in with a username and password:

Test User:
```admin``` / ```admin123```

The API can be tested using cURL, Postman, or any HTTP client.


## 📌 API Features  

### ✅ Retrieve product model data  
Fetch product information by entityId.  

  ```GET /model?entityId={id}```

### ✅ Fetch SKUs for a specific model
Retrieve all SKUs linked to a given entityId.

```GET /models/{entityId}/skus```

### ✅ Retrieve prices by SKU
Filter price details based on priceGroup and priceType.

```GET /models/{entityId}/skus/{skuID}/pricegroups```

### ✅ Filter prices by date range
Search for price records valid between two dates.

```GET /models/{entityId}/skus/{skuID}/prices-by-date?start_time=YYYYMMDD&end_time=YYYYMMDD```

### ✅ JWT Authentication
The API requires authentication for certain routes.

# 📂 Repository Structure

- ```main.py``` – Main FastAPI server
- ```auth.py``` – Authentication logic
- ```utils.py``` – Utility functions
- ```data.json``` – Test dataset (contains only one product model for API demonstration purposes)
