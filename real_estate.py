# %% [markdown]
# # Real Estate Prices
# The purpose of this machine learning model is to predict fair market prices for real estate sales. 

# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# %%
df = pd.read_csv("AmesHousing.csv")

# Data exploration 
print(df.head())
print(df.info())
print(df.columns)

# %%
# One-hot encode one column for each neighborhood and rejoin to dataframe 
ohe = pd.get_dummies(df['Neighborhood'], prefix="Neighborhood")

# Dimensionality reduction to 4 critical factors 
X = df[['Lot Area', 'Year Built', 'Gr Liv Area']]
X = X.join(ohe)

y = df['SalePrice']

print(X.columns)


# %%
#Training data v Test data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=32)


# %%
# Creates a LinearRegression model,
mlr = LinearRegression()

# %%
# Finds the coefficients(m) and the intercept value(b)
mlr.fit(X_train, y_train)

# %%
# Inputs values calculated by `.fit()` and the `x` values, plugs them into the multiple linear regression equation, and calculates the predicted y values.
y_predict = mlr.predict(X_test)

# %%
# Model 
# Housing features to see a fair market price

features = [
    'Lot Area', 'Year Built', 'Gr Liv Area',
    'Neighborhood_Blmngtn', 'Neighborhood_Blueste', 'Neighborhood_BrDale',
    'Neighborhood_BrkSide', 'Neighborhood_ClearCr', 'Neighborhood_CollgCr',
    'Neighborhood_Crawfor', 'Neighborhood_Edwards', 'Neighborhood_Gilbert',
    'Neighborhood_Greens', 'Neighborhood_GrnHill', 'Neighborhood_IDOTRR',
    'Neighborhood_Landmrk', 'Neighborhood_MeadowV', 'Neighborhood_Mitchel',
    'Neighborhood_NAmes', 'Neighborhood_NPkVill', 'Neighborhood_NWAmes',
    'Neighborhood_NoRidge', 'Neighborhood_NridgHt', 'Neighborhood_OldTown',
    'Neighborhood_SWISU', 'Neighborhood_Sawyer', 'Neighborhood_SawyerW',
    'Neighborhood_Somerst', 'Neighborhood_StoneBr', 'Neighborhood_Timber',
    'Neighborhood_Veenker'
]

# Ask user for input
neighborhood = input("Enter neighborhood (e.g., ClearCr, NWAmes, Veenker): ")
lot_area = input("Enter lot area (e.g., 3000, 5000, 7000): ")
year_built = input("Enter year built (e.g., 1925, 1975, 2025): ")
gr_liv_area = input("Enter square feet of the house (e.g., 1000, 2000, 3000): ")

# Build a dataframe with zeros
row = pd.DataFrame([[0] * len(features)], columns=features)

# Fill numeric features
row.loc[0, 'Lot Area'] = lot_area
row.loc[0, 'Year Built'] = year_built
row.loc[0, 'Gr Liv Area'] = gr_liv_area

# Activate the correct one-hot neighborhood
col_name = f'Neighborhood_{neighborhood}'
if col_name in row.columns:
    row.loc[0, col_name] = 1
else:
    print(f"Warning: {neighborhood} not a valid neighborhood")

# Predict
prediction = mlr.predict(row)
print("Predicted price:", "$",round(prediction[0], 2))

# %%
# Evaluation 
print("Train score:", mlr.score(X_train, y_train))
print("Test score:", mlr.score(X_test, y_test))

# %% [markdown]
# # Enterprise model
# ## Evaluation 
# Competition accuracy score (R²)> 90% 
# Objectively good accuracy ≥ 0.80
# Prototype models (demo) accuracy > 70% is satisfactory 
# If train score ≈ 0.95 but test score ≈ 0.70, the model overfits the data
# If train score is +- 5% of the test score, the model generalizes well, even if it’s not state-of-the-art accuracy
# Tree-based models (Random Forest, Gradient Boosting, XGBoost, LightGBM, CatBoost) can push R² to 0.85–0.95
# 
# ## Enterprise Model 
# x = sales_features = ['address', 'city', 'state', 'zip_code', 'latitude', 'longitude', 'acres', 'lot_size', 'square_feet', 'building_age', ['amenities'], ['schools'], ['universities']]
# y = selling_price = []
# 
# ## Income Based Valuation Model 
# x = income_features = ['revenue', 'salaries & fees', 'property_taxes', 'insurance', 'repairs_and_maintenance']
# y = income_based_valuation = []
# 
# ## Rent Prediction Model
# x = rent_features = ['square_feet', 'bedrooms', 'bathrooms', 'building_age']
# y = rent = []


