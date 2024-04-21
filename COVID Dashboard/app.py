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


if __name__=="__main__":
    app.layout=html.Div([
        html.H1("CoVID India View",style={"color":"#fff","text-align":"center","margin-top":"40px"}),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Total Cases",className="text-light"),
                        html.H4("600",className="text-light")
                    ],className="card-body")
                ],className="card bg-warning")
            ],className="col-md-3"),
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Active Cases", className="text-light"),
                        html.H4("600", className="text-light")
                    ],className="card-body")
                ],className="card bg-info")
            ],className="col-md-3"),
            html.Div([html.Div([
                    html.Div([
                        html.H3("Recovered", className="text-light"),
                        html.H4("600", className="text-light")
                    ],className="card-body")
                ],className="card bg-success")],className="col-md-3"),
            html.Div([html.Div([
                    html.Div([
                        html.H3("Deaths", className="text-light"),
                        html.H4("600", className="text-light")
                    ],className="card-body")
                ],className="card bg-danger")],className="col-md-3")
        ],className="row"),
        html.Div([
            html.Div([], className="col-md-6"),
            html.Div([], className="col-md-6"),
        ],className="row"),
        html.Div([
            html.Div([], className="col-md-12"),
],className="row")
    ],className="container")
    app.run_server(debug=True)