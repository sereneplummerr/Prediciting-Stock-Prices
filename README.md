# Data Visualization Project
This independent project demonstrates my proficiency in data visualization, model training, and analysis using Scikit-Learn. I focused on extracting insights from stock price data and evaluating model performance.

## AAPL Stock Price Prediction Using Support Vector Regression
I used Support Vector Regression (SVR) models to predict AAPL stock prices based on the past 30 days of data.

*For the Support Vector Regression (SVR) portion of this project, I initially relied on a YouTube video to get a grasp of the basic implementation steps. I followed the code walkthrough provided in the video to understand how to structure the SVR model in Python, as well as how to format the data and visualize the results. From there, I adapted the code to suit my own dataset and made improvements to fit my project needs. This approach allowed me to learn from an accessible example while still ensuring that I understood each step and could explain the rationale behind every part of the implementation.*


## *Overview* ##
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

## Synthetic Data Generation
- Cleaned and reformatted the dataset.
- Explored the distribution of closing prices using histograms.
- Used SMOTE (Synthetic Minority Over-sampling Technique) to attempt to balance classes.
- Suggested merging or removing sparse classes as a future step.
