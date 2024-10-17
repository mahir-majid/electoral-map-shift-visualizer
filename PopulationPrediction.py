from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import pandas as pd

from States import USA_STATES_DATA_1970_2020 

# Predicting the U.S. state populations for 2025 and 2030 using data trends from 1970 to 2020 
x = USA_STATES_DATA_1970_2020['Year'].values.reshape(-1, 1)
degree = 2
States_Population_Prediction_2030 = []

# Iterating through each state and making a population prediction in 2030 using 
# a polynomial regression model of degree 2
for i in range(1, len(USA_STATES_DATA_1970_2020.columns)):
    state = USA_STATES_DATA_1970_2020.columns[i]
    y = USA_STATES_DATA_1970_2020[state]
    poly_model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    poly_model.fit(x, y)
    poly_prediction = round(float(poly_model.predict([[2030]])[0]), 5)
    States_Population_Prediction_2030.append(poly_prediction)

# Organizing the predicted 2030 U.S. state populations into a DataFrame
States_Population_Prediction_2030_df = pd.DataFrame(States_Population_Prediction_2030).T

states = []

for i in range(1, len(USA_STATES_DATA_1970_2020.columns)):
    states.append(USA_STATES_DATA_1970_2020.columns[i])

States_Population_Prediction_2030_df.columns = states

print("DataFrame for Predicted U.S. States Population in 2030 (in millions)")
print(States_Population_Prediction_2030_df)