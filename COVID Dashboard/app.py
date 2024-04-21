import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

external_stylesheets= {
"href":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
"integrity":"sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" ,
"crossorigin":"anonymous",
}

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

if __name__=="__main__":
    app.run_server(debug=True)