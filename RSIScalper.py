import pandas as pd

df = {
    'Stock' : ['AAPL','TSLA','NVDA','AMD','GME'],
    'Price' : [180.50,245.30,502.00,156.20,25.80]
}

df = pd.DataFrame(df)
print(df)
print(df['Price'])

print(df.iloc[-2:])