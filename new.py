from dash import Dash, html, dash_table
import pandas as pd
import requests

app = Dash(__name__)

# Fetching data from the API
try:
    url = "https://www.balldontlie.io/api/v1/players"
    # headers = {
    #     "X-RapidAPI-Key": "92553ecf58msh5e3bfb1d615a421p1bd6cejsne10eac083a7c",
    #     "X-RapidAPI-Host": "americanfootballapi.p.rapidapi.com"
    # }
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['data'][0])  # Convert JSON data to DataFrame
    print(df.head())
except Exception as e:
    print("Error fetching data:", e)
    df = pd.DataFrame()  # Creating an empty DataFrame if data fetch fails

# Define columns
columns = [{'name': i, 'id': i} for i in df.columns]

#construct the layout of the app
app.layout = html.Div([
    html.Div(children='NBA Player Data'),
    dash_table.DataTable(
        data=df.to_dict('records'), columns=columns
        )
])

#run the app
if __name__ == '__main__':
    app.run_server(debug=True)
