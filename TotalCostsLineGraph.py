import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

df = pd.read_csv('Table02_NationalHealthExpendituresByType_BillionDollars_Normalized.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='LineGraphTest')