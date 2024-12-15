import pandas as pd
import numpy as np
import plotly.io as pio
from helper import line_plot, Overview_all

# Sample data for testing
dates = pd.date_range(start='2021-01-01', periods=100)
data = pd.DataFrame({
    'Date': dates,
    'Close': np.random.rand(100) * 100,
    'Open': np.random.rand(100) * 100,
    'High': np.random.rand(100) * 100,
    'Low': np.random.rand(100) * 100,
})

data.set_index('Date', inplace=True)

# Test line_plot function
line_fig = line_plot(data, 'Close', color='blue', width=1000, height=500)
line_fig.show()

# Test Overview_all function
overview_fig = Overview_all(data, title='Overview of Stock Prices', width=1000, height=500)
overview_fig.show()
