# predict.py

import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_price(square_feet):
    prediction = model.predict([[square_feet]])
    return prediction[0]

if __name__ == "__main__":
    # Example: Predict the price for a 1000 square foot house
    square_feet = 1000
    price = predict_price(square_feet)
    print(f"The predicted price for a house with {square_feet} square feet is ${price:.2f}")
