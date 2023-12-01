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
    dash_table.DataTable(
        id = 'player-table'
    )
])

# Callbacks
@app.callback(
    Output('player_details', 'children'),
    Output('player-table', 'data'),
    Output('player-table', 'columns'),
    Input('player-dropdown', 'value')
)

# create Callback function
def update_player_info(selected_player_idx):
    player = players_df.iloc[selected_player_idx]
    player_details = f"Name: {player['first_name']} {player['last_name']}"
    # handling nan values for height
    if pd.notna(player['height_feet']) and pd.notna(player['height_inches']):
        height = f"{player['height_feet']}'{player['height_inches']}\"" 
    else: 
        height = "Not Available"
    
    print(height)

    # Prepare table data and columns
    table_data = [{
        'Position': player['position'],
        'Height': height,
        'Team': player['team']['full_name'],
        'Division': player['team']['division'],
        'Weight': player['weight_pounds'] if pd.notna(player['weight_pounds']) else "Not Available"
    }]
    columns =  columns = [
        {"name": "Height", "id": "Height"},
        {"name": "Position", "id": "Position"},
        {"name": "Team", "id": "Team"},
        {"name": "Division", "id": "Division"},
        {"name": "Weight", "id": "Weight"}
    ]

    return player_details, table_data, columns


if __name__ == '__main__':
    app.run_server(debug=True)
