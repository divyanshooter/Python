import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

external_stylesheets= [{
"href":"https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
"rel":"stylesheet",
"integrity":"sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" ,
"crossorigin":"anonymous"

}]

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout=html.H1("Hello World!")

if __name__=="__main__":
    app.run_server(debug=True)