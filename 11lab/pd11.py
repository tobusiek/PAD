from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)
df = pd.read_csv('./winequelity.csv')
df.rename({'Unnamed: 0': 'idx'}, axis=1, inplace=True)
df.index = df['idx']
# del df['idx']


def generate_table(df, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), max_rows))
        ])
    ])


models = {
    'Regression': df.drop('pH', axis=1).columns,
    'Classification': df.drop('target', axis=1).columns
}

app.layout = html.Div([
    html.H4(children='Wines dataset'),
    generate_table(df),
    html.Br(),
    html.Div([
        html.Label('Choose model'),
        dcc.RadioItems(list(models.keys()), 'Regression', id='model'),
        html.Br(),
        html.Label('Choose parameter'),
        dcc.Dropdown(id='parameter'),
        dcc.Graph(id='graph')
    ])
])

@app.callback(
    Output('parameter', 'options'),
    Input('model', 'value'))
def set_parameters(selected_model):
    return [{'label':p, 'value':p} for p in models[selected_model]]


@app.callback(
    Output('graph', 'figure'),
    Input('model', 'value'),
    Input('parameter', 'value'))
def update_figure(model, parameter):
    if model == 'Regression': fig = px.scatter(df, x=parameter, y='pH')
    else: fig = px.box(df, x=parameter, y='target')
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
