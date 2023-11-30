from dash import Dash, html, dash_table, dcc, Output, Input
import pandas as pd
import requests

app = Dash(__name__)

# Fetching data from the API
try:
    url = "https://www.balldontlie.io/api/v1/players"
    data = requests.get(url).json() # get the response from the APi endpoint and turn it into a JSON
    players_df = pd.DataFrame(data['data'])  # Convert JSON data to DataFrame
except Exception as e:
    print("Error fetching data:", e)
    df = pd.DataFrame()  # Creating an empty DataFrame if data fetch fails


#construct the layout of the app
app.layout = html.Div([
    html.Div(children='NBA Player Data'),
    dcc.Dropdown(
        id = 'player-dropdown',
        options=[{'label': player['first_name'] + ' ' + player['last_name'] +'  |  ' + player['position'], 'value':idx } for idx, player in players_df.iterrows()],
        value=237
    ),

    dash_table.DataTable(id = 'player-table')
])

# Callbacks
@callback(
    Output
)

#run the app
if __name__ == '__main__':
    app.run_server(debug=True)
