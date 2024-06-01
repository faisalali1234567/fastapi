#web frame work
from fastapi import FastAPI
from enum import Enum

# Creation of instance
app = FastAPI()

# Create the endpoint
# @app.get("/hello")
# async def hello():
#     return "welcome to fast api  thankyou"

#http rest protocal
#creating a paremetric end point
@app.get("/hello/{name}")
async def hello(name):
    return f"welcome to fast api {name}"

class Availablecuisines(str,Enum):
    india = 'india'
    america = 'america'
    italy = 'italy'
    japan = 'japan'


food_items= {
    'india' : ['samosa', 'vadapav'],
    'america' : ['pizza', 'burger'],
    'italy' : ['pasta', 'pizza'],
    'japan' : ['sushi', 'ramen'],
}

valid_cusine = food_items.keys()


# @app.get("/get_cusine/{cusine}")
# async def cusinee(cusine):
#     if cusine not in ['india','america','italy','japan']:
#         return f"supported cusines are {valid_cusine}"
#     return food_items.get(cusine)


#inbuild data validation 
@app.get("/get_items/{cuisines}")
async def get_cusine(cuisines: Availablecuisines):
    return food_items.get(cuisines)


coupon_code ={
    1 : '10%',
    2 : '20%',
    3 : '30%'
}

@app.get("/coupon_code/{code}")
async def get_code(code: int):
    return {'discount_amount' : coupon_code.get(code)}
