from app.schemas import loan_input 
import numpy as np 
from app.models import (le_gender,
                        le_married,
                        le_education,
                        le_self_employed,
                        le_property_area,
                        pca_transformer,
                        Load_model)



def loan_approval(data : loan_input):
        Gender = le_gender.transform([data.Gender])[0]
        Married = le_married.transform([data.Married])[0]
        Education = le_education.transform([data.Education])[0]
        Self_Employed = le_self_employed.transform([data.Self_Employed])[0]
        Property_Area = le_property_area.transform([data.Property_Area])[0]


        X = np.array([[
            Gender,
            Married,
            Education,
            Self_Employed,
            data.Applicant_Income,
            Property_Area
        ]], dtype=np.float32)


        pca_transformers = pca_transformer.transform(X)

        prediction = Load_model(pca_transformers)

        return {
                'status' : 'Approved' if prediction[0][0] > 0.5 else "Not approved",
                'probability': round(float(prediction[0][0]), 2)


        }
