from dash import Dash, html, dash_table
import pandas as pd
import requests

app = Dash(__name__)

# Fetching data from the API
try:
    url = "https://americanfootballapi.p.rapidapi.com/api/american-football/search/brady"
    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
        "X-RapidAPI-Host": "americanfootballapi.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    df = pd.DataFrame(data)  # Convert JSON data to DataFrame
    print(df.head())
except Exception as e:
    print("Error fetching data:", e)
    df = pd.DataFrame()  # Creating an empty DataFrame if data fetch fails

app.layout = html.Div([
    html.Div(children='Fantasy Football'),
    dash_table.DataTable(data=df.to_dict('records'))
])

if __name__ == '__main__':
    app.run_server(debug=True)
