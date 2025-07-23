from fastapi import FastAPI
from pydantic import BaseModel, conlist
from typing import List, Optional
import pandas as pd
from model import recommend, output_recommended_recipes
from dotenv import load_dotenv
import os
import openai
from fastapi import Request
from pydantic import BaseModel
from openai import OpenAI, APIConnectionError  # include specific error

load_dotenv()  # load from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")
dataset = pd.read_csv('../Data/dataset.csv/dataset.csv')

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # uses key from .env

@app.post("/chat/")
def chat_endpoint(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for food and diet-related queries."},
                {"role": "user", "content": request.message}
            ],
            max_tokens=100,
            temperature=0.7,
        )
        return {"reply": response.choices[0].message.content}

    except APIConnectionError as ce:
        print(f"OpenAI API connection error: {ce}")
        return {"reply": "⚠️ Sorry, the chatbot is currently unreachable. Please try again shortly."}
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return {"reply": "❌ Something went wrong while processing your request. Please try again later."}


class params(BaseModel):
    n_neighbors: int = 5
    return_distance: bool = False

class PredictionIn(BaseModel):
    nutrition_input: conlist(float, min_items=9, max_items=9)
    ingredients: list[str] = []
    params: Optional[params]

class Recipe(BaseModel):
    Name: str
    CookTime: Optional[str] = None
    PrepTime: Optional[str] = None
    TotalTime: Optional[str] = None
    RecipeIngredientParts: list[str]
    Calories: float
    FatContent: float
    SaturatedFatContent: float
    CholesterolContent: float
    SodiumContent: float
    CarbohydrateContent: float
    FiberContent: float
    SugarContent: float
    ProteinContent: float
    RecipeInstructions: list[str]

class PredictionOut(BaseModel):
    output: Optional[List[Recipe]] = None

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/predict/", response_model=PredictionOut)
def update_item(prediction_input: PredictionIn):
    recommendation_dataframe = recommend(
        dataset,
        prediction_input.nutrition_input,
        prediction_input.ingredients,
        prediction_input.params.dict()
    )
    output = output_recommended_recipes(recommendation_dataframe)
    if output is None:
        return {"output": None}
    else:
        return {"output": output}
