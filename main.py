from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello():
    return "Hello WebApp"

@app.get("/bye")
async def hello():
    return "Goodbye WebApp"

@app.get("/sleep")
async def hello():
    return "Goodnight WebApp"

@app.get("/smile")
async def hello():
    return ":-) <hi"

@app.get("/hello")
async def hello(name):
    return  {"message":"hello{0}".format(name)}

@app.post("/study")
async def createstudy(req: Request):
    body = await req.body()
    return body