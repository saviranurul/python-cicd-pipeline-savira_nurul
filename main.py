from sources import calc
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num1:float
    num2:float

@app.get("/")
def read_root():
    return {"message": "Welcome to Savira Python Simple App"}


@app.post("/calc")
def read_item(data:NumberInput):
    total = str(calc.add2(str(data.num1), str(data.num2)))
    return {"number_input": data,"total":total}