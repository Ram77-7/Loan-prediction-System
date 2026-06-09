from pydantic import BaseModel 

class loan_input(BaseModel):
    Gender : str 
    Married : str 
    Education : str 
    Self_Employed : str 
    Applicant_Income : int 
    Property_Area : str
