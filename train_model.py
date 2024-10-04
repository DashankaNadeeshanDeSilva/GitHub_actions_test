# This script trains a simple Linear regression model on dummy data and saves the model.

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Create a simple dataset
data = {
    'square_feet': [750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200],
    'price': [150000, 160000, 170000, 180000, 190000, 200000, 210000, 220000, 230000, 240000]
}
df = pd.DataFrame(data)

# Train a simple Linear Regression model
X = df[['square_feet']]
y = df['price']
model = LinearRegression()
model.fit(X, y)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
