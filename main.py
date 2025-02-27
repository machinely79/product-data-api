
from fastapi import FastAPI, HTTPException, Depends, Query
from auth import get_current_user
from utils import read_json, get_model_by_id, get_skus_by_model, get_prices_by_sku, get_prices_by_date

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Product Data API"}

# Get model data
@app.get("/model")
def read_model(entityId: str, user: str = Depends(get_current_user)):
    data = read_json("data.json")
    return get_model_by_id(entityId, data)

# Get SKUs for a model
@app.get("/models/{entityId}/skus")
def read_skus(entityId: str, user: str = Depends(get_current_user)):
    data = read_json("data.json")
    return get_skus_by_model(entityId, data)


# Get prices for a SKU
@app.get("/models/{entityId}/skus/{skuID}/pricegroups")
def read_prices(entityId: str, skuID: str, priceGroup: str | None = None, priceType: str | None = None, user: str = Depends(get_current_user)):
    data = read_json("data.json")
    return get_prices_by_sku(entityId, skuID, priceGroup, priceType, data)


# Get prices by date
@app.get("/models/{entityId}/skus/{skuID}/prices-by-date")
def read_prices_by_date(
    entityId: str,
    skuID: str,
    start_time: str = Query(None, description="Start date in format YYYYMMDD"),
    end_time: str = Query(None, description="End date in format YYYYMMDD"),
    user: str = Depends(get_current_user)
):
    data = read_json("data.json")  
    return get_prices_by_date(start_time, end_time, entityId, skuID, data)


# # Get prices by date
# @app.get("/prices-by-date")
# def read_prices_by_date(
#     start_time: str = Query(None, description="Start date in format YYYYMMDD"),
#     end_time: str = Query(None, description="End date in format YYYYMMDD")
# ):
#     data = read_json("data.json")
#     return get_prices_by_date(start_time, end_time, data)
