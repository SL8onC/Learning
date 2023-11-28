from dash import Dash, dcc, html, Input, Output, dash_table
import pandas as pd

app = Dash(__name__)

#incorparte the data
df = pd.read_csv('https://api.fantasynerds.com/v1/nfl/weekly-rankings?apikey=TGQCQW6FFTPQM73EEH89Gformat=')
print(df.head())


app.layout = html.Div([
    html.Div(children='Fantasy Football'),
    dash_table.DataTable(data=df.to_dict('records'))
])

if __name__ == '__main__':
    app.run(debug=True)