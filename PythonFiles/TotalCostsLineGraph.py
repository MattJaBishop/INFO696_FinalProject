# import plotly

# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as FF

# import numpy as np
# import pandas as pd

# df = pd.read_csv('Table02_NationalHealthExpendituresByType_BillionDollars_Normalized.csv')

# sample_data_table = FF.create_table(df.head())
# py.iplot(sample_data_table, filename='LineGraphTest')

# trace1 = go.Scatter(
#                     x=df['Year'], y=df['Cost'], # Data
#                     mode='lines', name='Cost' # Additional options
#                    )
# trace2 = go.Scatter(x=df['Year'], y=df['sinx'], mode='lines', name='sinx' )
# trace3 = go.Scatter(x=df['Year'], y=df['cosx'], mode='lines', name='cosx')

# layout = go.Layout(title='Simple Plot from csv data',
#                    plot_bgcolor='rgb(230, 230,230)')

# fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# # Plot data in the notebook
# py.iplot(fig, filename='LineGraphTestCSV')

import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

py.iplot(data, filename='basic-line')