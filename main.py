from fastapi import FastAPI, Query
import uvicorn
import pandas as pd
from pandas.core.computation.common import result_type_many

app = FastAPI()

def random_items():
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    result_items = movies_df.sample(n=10)
    return result_items

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/all/")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    return {"result": f"선택한 장르{genre} "}

if __name__== '__main __':
    uvicorn.run(app, host='127.0.0.1', port=8000)
