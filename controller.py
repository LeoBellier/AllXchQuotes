import uvicorn
from fastapi import FastAPI
from get_quotes import get_all


app = FastAPI()


@app.get("/")
async def get_index():
    quotes = get_all()
    print(quotes)
    return {'message': quotes}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
