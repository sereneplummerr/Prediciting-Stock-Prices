import yfinance as yf
import pandas as pd

#Download historical data for Apple Inc. (AAPL) for the last 30 days with daily intervals
aapl_data = yf.download("AAPL", period="30d", interval="1d")

#Show in terminal
print(aapl_data)

#Save the data to a CSV file
aapl_data.to_csv("AAPL_30d.csv")