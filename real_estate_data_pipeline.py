# %%
# Data pipeline 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

df = pd.read_csv("AmesHousing.csv")
print("Ames, Iowa real estate selling price regression.")

X = df[['Neighborhood', 'Lot Area', 'Year Built', 'Gr Liv Area']]
y = df['SalePrice']

categorical = ['Neighborhood']
numeric = ['Lot Area', 'Year Built', 'Gr Liv Area']

# Preprocessing: OHE for categorical, passthrough for numeric
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
        ('num', 'passthrough', numeric)
    ]
)

# Data pipeline
mlr = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit
mlr.fit(X_train, y_train)

#Evaluation
# print("Training accuracy (R²): ", f"{mlr.score(X_train, y_train)*100:,.2f}%")
# print("Test accuracy (R²): ", f"{mlr.score(X_test, y_test)*100:,.2f}%")

# User input
neighborhood = input("Enter neighborhood (e.g., ClearCr, NWAmes, Veenker): ")
lot_area = input("Enter lot area (e.g., 3000, 5000, 7000): ")
year_built = input("Enter year built (e.g., 1925, 1975, 2025): ")
gr_liv_area = input("Enter square feet of the house (e.g., 1000, 2000, 3000): ")

# Predicted new house selling price
open_house = pd.DataFrame([{
    'Neighborhood': neighborhood,
    'Lot Area': lot_area,
    'Year Built': year_built,
    'Gr Liv Area': gr_liv_area
}])

prediction = mlr.predict(open_house)[0]
print("Predicted price:", f"${prediction:,.2f}")













