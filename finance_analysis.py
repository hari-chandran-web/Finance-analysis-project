import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set your stock tickers
tickers = ['AAPL', 'MSFT', 'GOOGL']

# Download historical data
data = yf.download(tickers, start='2020-01-01', end='2024-12-31', auto_adjust=False)['Adj Close']

# Drop any missing data
data.dropna(inplace=True)

# Daily returns
returns = data.pct_change().dropna()

# Plot stock prices
plt.figure(figsize=(12, 6))
data.plot()
plt.title('Stock Price History')
plt.ylabel('Price (USD)')
plt.xlabel('Date')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot daily returns
plt.figure(figsize=(12, 6))
returns.plot()
plt.title('Daily Returns')
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate average returns and volatility
avg_returns = returns.mean() * 252
volatility = returns.std() * np.sqrt(252)

# Show Risk & Return
print("\nAverage Annual Returns:")
print(avg_returns)
print("\nAnnual Volatility:")
print(volatility)

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(returns.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix of Returns")
plt.tight_layout()
plt.show()

# Optional: Cumulative returns plot
cumulative_returns = (1 + returns).cumprod()
cumulative_returns.plot(figsize=(12, 6))
plt.title('Cumulative Returns')
plt.grid(True)
plt.tight_layout()
plt.show()
