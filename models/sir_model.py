import numpy as np
from scipy.integrate import odeint
import plotly.graph_objs as go

def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

def run_sir_model(df, beta=0.3, gamma=0.1, population=1000000, days=100):
    """
    Run the SIR model with customizable parameters
    
    Args:
        df (pd.DataFrame): Input data
        beta (float): Infection rate
        gamma (float): Recovery rate
        population (int): Total population size
        days (int): Number of days to simulate
        
    Returns:
        plotly.graph_objs.Figure: SIR model visualization
    """
    # Initialize initial conditions
    I0 = df['total_cases'].iloc[0]
    R0 = 0
    S0 = population - I0 - R0
    
    # Create time vector
    t = np.linspace(0, days, days)
    
    # Initial conditions vector
    y0 = S0/population, I0/population, R0/population
    
    # Integrate the SIR equations over time
    ret = odeint(sir_model, y0, t, args=(beta, gamma))
    S, I, R = ret.T
    
    # Create plotly figure
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(x=t, y=S*population, mode='lines', name='Susceptible', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=t, y=I*population, mode='lines', name='Infected', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=t, y=R*population, mode='lines', name='Recovered', line=dict(color='green')))
    
    # Update layout
    fig.update_layout(
        title='SIR Model Simulation',
        xaxis_title='Time (days)',
        yaxis_title='Number of Individuals',
        hovermode='closest',
        showlegend=True,
        legend_title='Compartments',
        template='plotly_white'
    )
    
    return fig
