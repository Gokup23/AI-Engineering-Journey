import csv

data = [
    ['Ticker', 'Price', 'Quantity', 'Type'],
    ['AAPL', '150.50', '10', 'BUY'],
    ['GOOGL', '2800.00', '2', 'BUY'],
    ['TSLA', 'invalid_price', '5', 'SELL'],  # ❌ Bad Data (ValueError)
    ['AMZN', '3300.00', '-1', 'BUY'],       # ❌ Logical Error (Negative Qty)
    ['MSFT', '300.00', '10', 'BUY'],
    ['NFLX', '500.00', 'N/A', 'SELL']       # ❌ Bad Data (ValueError)
]

with open('raw_trades.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Raw data csv file is created !")