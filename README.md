# AAPL Stock Price Prediction Using Support Vector Regression
This project predicts Apple Inc. (AAPL) stock prices using Support Vector Regression (SVR) in Python. The implementation is based on the concepts demonstrated in Siraj Raval’s "Predicting Stock Prices" tutorial, which served as the initial guide for this model.

## Overview
The model analyzes 30 days of historical AAPL stock data and predicts future prices using the day of the month as the input feature. It compares the performance of three different SVR kernels:

* Linear

* Polynomial (degree 2)

* Radial Basis Function (RBF)

The script:

* Reads data from AAPL_30d.csv.

* Extracts the day from the date as a numerical input.

* Trains three SVR models.

* Visualizes each model's predictions compared to actual prices using Matplotlib.

* Outputs predicted prices for a specified day (e.g., day 29).
