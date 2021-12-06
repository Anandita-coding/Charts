import pandas as pd
import plotly_express as px

df = pd.read_csv("CSV/CovidData.csv")  
fig = px.scatter(df,x = "Date",y = "Cases",color = "Country",title = "Covid Cases",size_max = 30)
fig.show()

fig = px.bar(df,x = "Date",y = "Cases",color = "Country",title = "Covid Cases")
fig.show()

fig = px.pie(df, values='Date', names='Cases', title='Covid Cases')
fig.show()

data = px.line(df,x="Date",y="Cases",color = "Country",title="Covid Cases")
data.show()