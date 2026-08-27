# logistics-predictive-optimization
Project 4 – Predictive Modeling and Optimization in Logistics Systems

## Overview

This project demonstrates how **predictive modeling** and **route optimization** can be combined to support last-mile logistics operations.

The business problem is to predict delivery time using operational factors such as distance, traffic, weather, package count, vehicle load, delivery priority, and warehouse delay. The predicted information can then support dispatching and route-planning decisions.

> **Note:** The dataset in this repository is synthetic and was created for academic/project demonstration purposes. It does not represent real company data.

## Objectives

- Predict delivery duration in minutes.
- Compare Linear Regression with Random Forest Regression.
- Evaluate models using MAE, RMSE, and R².
- Identify important operational features.
- Demonstrate a simple nearest-neighbor route optimization heuristic.
- Show how predictive analytics can support logistics decisions.

## Dataset

`logistics_delivery_data.csv` contains 500 synthetic delivery records.

### Features

| Feature | Description |
|---|---|
| distance_km | Delivery distance in kilometers |
| traffic_index | Traffic severity from 1 to 10 |
| weather_index | Weather severity from 1 to 5 |
| package_count | Number of packages |
| vehicle_load_pct | Vehicle utilization percentage |
| priority | 1 = priority, 0 = normal |
| warehouse_delay_min | Warehouse/loading delay in minutes |
| delivery_time_min | Target delivery duration in minutes |

## Models

### 1. Linear Regression
Used as an interpretable baseline model.

### 2. Random Forest Regression
Used to capture nonlinear relationships and interactions between logistics variables.

## Evaluation

The data is split into:

- 80% training data
- 20% testing data
- Random seed: `42`

The experiment produced approximately:

| Model | MAE (min) | RMSE (min) | R² |
|---|---:|---:|---:|
| Linear Regression | 6.27 | 7.49 | 0.872 |
| Random Forest | 7.59 | 9.17 | 0.808 |

For this synthetic experiment, **Linear Regression performed better** on the held-out test set.

## Route Optimization

A small delivery network with one depot and 12 delivery locations is used.

The project compares:

1. A fixed sequential route.
2. A nearest-neighbor route heuristic.

In the simulated network, the nearest-neighbor heuristic reduced route distance by approximately **19.6%** compared with the fixed sequential route.

This is only a demonstration. A production logistics optimizer should include real road-network distances, vehicle capacity, delivery time windows, driver hours, service time, and traffic conditions.

## How to Run

Install the required libraries:

```bash
pip install numpy pandas scikit-learn
```

Run delivery-time prediction:

```bash
python logistics_prediction.py
```

Run route optimization:

```bash
python route_optimization.py
```

## Project Structure

```text
project4/
├── README.md
├── logistics_delivery_data.csv
├── logistics_prediction.py
├── route_optimization.py
└── Project_4_Report.docx
```

## Business Recommendations

- Use predicted delivery duration to improve ETA estimates.
- Identify high-risk deliveries before dispatch.
- Combine predicted travel/service times with route planning.
- Add real traffic and road-network data before deployment.
- Track MAE, RMSE, on-time delivery rate, route distance, fuel usage, and operating cost.
- Retrain the model periodically using recent operational data.

## Limitations

The data is synthetic and the route model uses Euclidean distance rather than real road travel time. Therefore, the results demonstrate the methodology rather than real-world performance.

## Author

Project 4 – Predictive Modeling and Optimization in Logistics Systems