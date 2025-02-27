import json
from datetime import datetime
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# Function to read JSON file
def read_json(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


# Function to get model by entityId
def get_model_by_id(entityId, data):
    if data.get("entityId") == entityId:
        return JSONResponse(content=jsonable_encoder(data))
    raise HTTPException(status_code=404, detail=f"Model with entityId: {entityId} was not found.")


# Function to get SKUs for a model
def get_skus_by_model(entityId, data):
    if data.get("entityId") == entityId:
        filtered_data = [
            {
                "entityId": obj["entityId"],
                "supplierSkuNumber": obj["supplierSkuNumber"],
                "descriptionLong": obj["descriptionLong"],
                "descriptionShort": obj["descriptionShort"],
                "colorName": obj["colorName"],
                "size": obj["size"],
                "codes": obj["codes"]
            }
            for obj in data.get("skus", [])
        ]
        return JSONResponse(content=jsonable_encoder(filtered_data))

    raise HTTPException(status_code=404, detail=f"SKUs for model entityId: {entityId} were not found.")


# Function to get prices for a SKU
def get_prices_by_sku(entityId, skuID, priceGroup, priceType, data):
    if data.get("entityId") != entityId or not any(sku["entityId"] == skuID for sku in data.get("skus", [])):
        raise HTTPException(status_code=404, detail=f"Prices with model entityId: {entityId} and skuID: {skuID} not found.")
    
    # Filter prices by priceGroup and priceType
    filtered_prices = []
    for sku in data["skus"]:
        if sku["entityId"] == skuID:
            for price in sku["prices"]:
                if (priceGroup is None or price["priceGroup"] == priceGroup) and (priceType is None or price["priceType"] == priceType):
                    filtered_prices.append(price)

    if filtered_prices:
        return JSONResponse(content=jsonable_encoder(filtered_prices))

    raise HTTPException(status_code=404, detail="No matching price data found.")


# Function to filter prices by date range for a specific SKU and entityId
def get_prices_by_date(start_time, end_time, entityId, skuID, data):
    if start_time is None or end_time is None:
        raise HTTPException(status_code=400, detail="Both start_time and end_time must be provided.")
    
    # Convert start_time and end_time to datetime objects
    try:
        start_dt = datetime.strptime(start_time, "%Y%m%d")
        end_dt = datetime.strptime(end_time, "%Y%m%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYYMMDD.")

    
    if data.get("entityId") != entityId:
        raise HTTPException(status_code=404, detail=f"Model with entityId {entityId} not found.")

    # Filter prices by entityId and skuID
    filtered_prices = []
    for sku in data.get("skus", []):
        if sku["entityId"] == skuID:
            for price in sku.get("prices", []):
                try:
                    price_date = datetime.strptime(price["validFrom"][:8], "%Y%m%d")
                    if start_dt <= price_date <= end_dt:
                        filtered_prices.append(price)
                except ValueError:
                    continue  

    if not filtered_prices:
        raise HTTPException(status_code=404, detail=f"No prices found for entityId {entityId}, skuID {skuID} in the given date range.")

    return JSONResponse(content=jsonable_encoder(filtered_prices))



# Function to filter prices by date range
# def get_prices_by_date(start_time, end_time, data):
#     if start_time is None or end_time is None:
#         raise HTTPException(status_code=400, detail="Both start_time and end_time must be provided.")

#     try:
#         start_dt = datetime.strptime(start_time, "%Y%m%d")
#         end_dt = datetime.strptime(end_time, "%Y%m%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use YYYYMMDD.")

#     filtered_prices = []
#     for sku in data.get("skus", []):
#         for price in sku.get("prices", []):
#             try:
#                 price_date = datetime.strptime(price["validFrom"][:8], "%Y%m%d") 
#                 if start_dt <= price_date <= end_dt:
#                     filtered_prices.append(price)
#             except ValueError:
#                 continue  

#     if not filtered_prices:
#         raise HTTPException(status_code=404, detail="No prices found in the given date range.")

#     return JSONResponse(content=jsonable_encoder(filtered_prices))
