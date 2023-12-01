from dash import Dash, html, dash_table, dcc, Output, Input
import pandas as pd
import requests

app = Dash(__name__)

# Fetching data from the API
try:
    url = "https://www.balldontlie.io/api/v1/players"
    data = requests.get(url).json() # get the response from the APi endpoint and turn it into a JSON
    players_df = pd.DataFrame(data['data'])  # Convert JSON data to DataFrame
    print(players_df.head())
except Exception as e:
    print("Error fetching data:", e)
    df = pd.DataFrame()  # Creating an empty DataFrame if data fetch fails


#construct the layout of the app
app.layout = html.Div([
    html.Div(children='NBA Player Data'),
    dcc.Dropdown(
        id = 'player-dropdown',
        options=[{'label': player['first_name'] + ' ' + player['last_name'] +'  |  ' + player['position'], 'value':idx } for idx, player in players_df.iterrows()],
        value=0
    ),
    html.Div(id = 'player_details'),
    dash_table.DataTable(id = 'player-table')
])

# Callbacks
@app.callback(
    Output('player_details', 'children'),
    Output('player-table', 'columns'),
    Output('player-table', 'data'),
    Input('player-dropdown', 'value')
)

# create Callback function
def update_player_info(selected_player_idx):
    player = players_df.iloc[selected_player_idx]
    player_details = f"Name: {player['first_name']} {player['last_name']}"
    height = f"Name: {player['height_feet']}'{player['height_inches']}\"" if player['height_feet'] and player['height_inches'] else "Not Available"
    #handling null values for player height ^ 
    # using the f-string as a shorthand for concatenation

    # Prepare table data and columns
    table_data = [{
        'Height': height,
        'Position': player['position'],
        'Team': player['team']['full_name'],
        'Division': player['team']['division']
        'Division': player['division']
    }]
    columns = [{"id": i, "name":i} for i in table_data[0].keys()]

    return player_details, table_data, columns


if __name__ == '__main__':
    app.run_server(debug=True)
