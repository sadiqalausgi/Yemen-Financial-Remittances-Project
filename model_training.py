
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def train_predictive_model(file_path):
    df = pd.read_csv(file_path)

    # Prepare the data for modeling
    X = df[["Year"]]
    y = df["Remittances"]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\nModel Evaluation:")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared (R2): {r2:.2f}")

    # Predict future remittances (e.g., for 2024-2030)
    future_years = np.array(range(2024, 2031)).reshape(-1, 1)
    future_predictions = model.predict(future_years)

    future_df = pd.DataFrame({
        "Year": future_years.flatten(),
        "Predicted_Remittances": future_predictions
    })
    print("\nFuture Remittance Predictions:")
    print(future_df)

    return model, mse, r2, future_df

if __name__ == "__main__":
    file_path = "yemen_remittances_cleaned.csv"
    model, mse, r2, future_predictions_df = train_predictive_model(file_path)
    future_predictions_df.to_csv("yemen_remittances_predictions.csv", index=False)
    print("Model trained and future predictions saved to yemen_remittances_predictions.csv")


