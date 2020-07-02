import plotly.graph_objects as go
import pandas
from datetime import datetime
filename = input("Please enter your csv file name: \n")
df = pandas.read_csv(filename)

candlestick = go.Candlestick(x=df['Timestamp'], 
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])

fig = go.Figure(data=[candlestick])
fig.show()