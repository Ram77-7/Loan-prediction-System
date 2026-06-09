from fastapi import FastAPI
from pydantic import BaseModel 
from app.schemas import loan_input
from app.predict import loan_approval
app = FastAPI(title = 'loan-approval',
              version = '1.0',
              description= 'Based on input data it predicts wheather loan is approved or not')


class Input(BaseModel):
    Name : str
    Age : int 
    Gender : str 
    Education : str

@app.get('/')
def home():
    return {'message' : 'Welcome to loan prediction app'}

@app.post('/info')
def info(data:Input):
    return f"Hi {data.Name}, and your age is  {data.Age}, you are a {data.Gender}, your education background is {data.Education}"

@app.post('/predict')
def predict_loan(data : loan_input):
    predict = loan_approval(data)

    return {
        'loan_status' : predict,
    }





    