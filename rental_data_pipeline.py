# %%
# Data pipeline 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

df = pd.read_csv("manhattan.csv")
print("Apartment rent regression.")

X = df[['bedrooms', 'bathrooms', 'size_sqft', 'building_age_yrs', 
        'floor', 'has_elevator', 'has_roofdeck']]
y = df[['rent']]

# Data pipeline
mlr = Pipeline(steps=[
    ('regressor', LinearRegression())
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model fit
mlr.fit(X_train, y_train)
print("Training accuracy (R²): ", f"{mlr.score(X_train, y_train)*100:,.2f}%")
print("Test accuracy (R²): ", f"{mlr.score(X_test, y_test)*100:,.2f}%")

# User input
bedrooms = input("Enter the number of bedrooms (e.g., 1, 2, 3): ")
bathrooms = input("Enter the number of bathrooms (e.g., 1, 2, 3): ")
size = input("Enter square feet of the apartment (e.g., 1000, 2000, 3000): ")
age = input("Enter the age of the building (e.g., 5 , 50, 100): ")
floor = input("What floor is the apartment on? : ")
elevator = input("Does the building have an elevator? (1 for yes, 0 for no): ")
roofdeck = input("Does the building have a roof deck? (1 for yes, 0 for no): ")

# Predicted rent
rent = pd.DataFrame([{
    'bedrooms': int(bedrooms),
    'bathrooms': int(bathrooms),
    'size_sqft': int(size),
    'building_age_yrs': int(age), 
    'floor': int(floor), 
    'has_elevator': int(elevator), 
    'has_roofdeck': int(roofdeck)
}])

prediction = mlr.predict(rent)[0]
#print("Predicted rent:", prediction[0])

print("Predicted monthly rent: ", f"${prediction[0]:,.2f}")