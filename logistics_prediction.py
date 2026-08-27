"""
Project 4: Predictive Modeling and Optimization in Logistics Systems
Delivery Time Prediction
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_FILE = "logistics_delivery_data.csv"

df = pd.read_csv(DATA_FILE)

X = df.drop(columns=["delivery_time_min"])
y = df["delivery_time_min"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=250,
        random_state=42,
        max_depth=10,
        min_samples_leaf=2
    )
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)

    print(f"{name}")
    print(f"MAE : {mae:.2f} minutes")
    print(f"RMSE: {rmse:.2f} minutes")
    print(f"R2  : {r2:.3f}")
    print("-" * 40)

# Feature importance for Random Forest
rf = models["Random Forest"]
importance = pd.Series(
    rf.feature_importances_, index=X.columns
).sort_values(ascending=False)

print("Random Forest feature importance:")
print(importance)
