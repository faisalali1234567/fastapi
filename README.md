# fastapi
Details about the FASTAPI Framework its utilizations as the backend severe and benefits over the other frame works

FastApi
 
Commands to install api
Pip install fastapi

Pip install uvicorn

Different type of end points 

SQL WORK BENCH	 vs  FAST API

C	CREATE	 P	POST

R	READ	   G	GET

U	UPDATE	 P	PUT

D	DELETE	 D	DELETE

 
Simple end point

@app.get("/hello/{name}")

async def hello(name):

    return f"welcome to fast api {name}"

inbuilt formation then

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

@app.get("/get_items/{cuisines}")

async def get_cusine(cuisines: Availablecuisines):

    return food_items.get(cuisines)

we run command in terminal as 

uvicorn main:app –reload

then we take the fast api server path http://127.0.0.1:8000/

paste in google with http://127.0.0.1:8000/get_items/india

Creation of document / front end automatically

http://127.0.0.1:8000/docs
 
http://127.0.0.1:8000/redoc
 
