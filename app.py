import dash
from dash import html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from models.sir_model import run_sir_model
import datetime

# Load sample data
df = pd.read_csv("data/sample_data.csv")

app = dash.Dash(__name__,
               external_stylesheets=[
                   'https://codepen.io/chriddyp/pen/bWLwgP.css'
               ])
app.title = "Advanced Epidemiological Dashboard"

app.layout = html.Div([
    html.Div([
        html.H1("Advanced Epidemiological Dashboard", style={'textAlign': 'center'}),
        html.Div([
            html.Label("Select Location:", style={'marginRight': '10px'}),
            dcc.Dropdown(
                id='location-dropdown',
                options=[{'label': c, 'value': c} for c in df['location'].unique()],
                value=df['location'].unique()[0],
                clearable=False,
                style={'width': '200px'}
            ),
        ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'}),
        
        html.Div([
            html.Label("Date Range:", style={'marginRight': '10px'}),
            dcc.DatePickerRange(
                id='date-picker',
                start_date=df['date'].min(),
                end_date=df['date'].max(),
                display_format='YYYY-MM-DD',
                style={'marginRight': '20px'}
            ),
            
            html.Label("Visualization Type:", style={'marginRight': '10px'}),
            dcc.RadioItems(
                id='viz-type',
                options=[
                    {'label': 'Line Chart', 'value': 'line'},
                    {'label': 'Bar Chart', 'value': 'bar'},
                    {'label': 'Area Chart', 'value': 'area'}
                ],
                value='line',
                labelStyle={'display': 'inline-block', 'marginRight': '10px'}
            )
        ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '20px'}),
        
        html.Div([
            html.Label("SIR Model Parameters:", style={'marginRight': '10px'}),
            html.Div([
                html.Label("Infection Rate (β):", style={'marginRight': '10px'}),
                dcc.Input(id='beta-input', type='number', value=0.3, min=0, max=1, step=0.01),
                html.Label("Recovery Rate (γ):", style={'marginRight': '10px'}),
                dcc.Input(id='gamma-input', type='number', value=0.1, min=0, max=1, step=0.01),
                html.Label("Population Size:", style={'marginRight': '10px'}),
                dcc.Input(id='population-input', type='number', value=1000000, min=1000, step=1000)
            ], style={'display': 'flex', 'alignItems': 'center', 'flexWrap': 'wrap'})
        ], style={'marginBottom': '20px'}),
        
        html.Button('Export Data', id='export-btn', n_clicks=0),
        html.Div(id='export-status', style={'marginTop': '10px'})
    ], style={'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '8px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='cases-graph'),
            dcc.Graph(id='sir-model-graph')
        ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '20px'})
    ], style={'padding': '20px'})
])

@app.callback(
    [Output("cases-graph", "figure"),
     Output("sir-model-graph", "figure")],
    [Input("location-dropdown", "value"),
     Input("date-picker", "start_date"),
     Input("date-picker", "end_date"),
     Input("viz-type", "value"),
     Input("beta-input", "value"),
     Input("gamma-input", "value"),
     Input("population-input", "value")]
)
def update_dashboard(location, start_date, end_date, viz_type, beta, gamma, population):
    dff = df[(df["location"] == location) & 
            (df["date"] >= start_date) & 
            (df["date"] <= end_date)]
    
    if viz_type == 'line':
        fig1 = px.line(dff, x="date", y="total_cases", 
                      title=f"{viz_type.title()} Chart: Total Cases in {location}")
    elif viz_type == 'bar':
        fig1 = px.bar(dff, x="date", y="total_cases", 
                     title=f"{viz_type.title()} Chart: Total Cases in {location}")
    else:  # area
        fig1 = px.area(dff, x="date", y="total_cases", 
                      title=f"{viz_type.title()} Chart: Total Cases in {location}")
    
    fig2 = run_sir_model(dff, beta=beta, gamma=gamma, population=population)
    
    return fig1, fig2

@app.callback(
    Output("export-status", "children"),
    [Input("export-btn", "n_clicks")],
    [State("location-dropdown", "value"),
     State("date-picker", "start_date"),
     State("date-picker", "end_date")]
)
def export_data(n_clicks, location, start_date, end_date):
    if n_clicks > 0:
        dff = df[(df["location"] == location) & 
                (df["date"] >= start_date) & 
                (df["date"] <= end_date)]
        
        filename = f"epidemiology_data_{location}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        dff.to_csv(filename, index=False)
        
        return html.Div([
            html.P(f"Data exported to {filename}", style={'color': 'green'}),
            html.A("Download", href=f"/{filename}", download=filename)
        ])
    return ""

if __name__ == "__main__":
    app.run(debug=True)
