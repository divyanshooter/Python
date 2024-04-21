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

patients=pd.read_csv('IndividualDetails.csv')
total=patients.shape[0]
active=patients[patients['current_status']=='Hospitalized'].shape[0]
recovered=patients[patients['current_status']=='Recovered'].shape[0]
deaths=patients[patients['current_status']=='Deceased'].shape[0]

covid=pd.read_csv('covid_19_india.csv',parse_dates=["Date"])
covid_date=covid.groupby('Date')['Confirmed'].sum().reset_index()

agewise=pd.read_csv("AgeGroupDetails.csv")

options=[
    {"label":"All","value":"All"},
    {"label":"Hospitalized","value":"Hospitalized"},
    {"label":"Recovered","value":"Recovered"},
    {"label":"Deceased","value":"Deceased"},
]


app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout=html.Div([
        html.H1("COVID-19 India View",style={"color":"#fff","text-align":"center","margin-top":"40px"}),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Total Cases",className="text-light"),
                        html.H4(total,className="text-light")
                    ],className="card-body")
                ],className="card bg-warning")
            ],className="col-md-3"),
            html.Div([
                html.Div([
                    html.Div([
                        html.H3("Active Cases", className="text-light"),
                        html.H4(active, className="text-light")
                    ],className="card-body")
                ],className="card bg-info")
            ],className="col-md-3"),
            html.Div([html.Div([
                    html.Div([
                        html.H3("Recovered", className="text-light"),
                        html.H4(recovered, className="text-light")
                    ],className="card-body")
                ],className="card bg-success")],className="col-md-3"),
            html.Div([html.Div([
                    html.Div([
                        html.H3("Deaths", className="text-light"),
                        html.H4(deaths, className="text-light")
                    ],className="card-body")
                ],className="card bg-danger")],className="col-md-3")
        ],className="row mt-5"),
        html.Div([
            html.Div([
                dcc.Graph(id="Line",figure=go.Figure(data= go.Line(x=covid_date["Date"],y=covid_date["Confirmed"]),
                                            layout=go.Layout(title="Day by Day Analysis")))
            ], className="col-md-6 mt-5"),
            html.Div([
                dcc.Graph(id="Pie", figure=go.Figure(data=go.Pie(labels=agewise["AgeGroup"], values=agewise["TotalCases"]),
                                                      layout=go.Layout(title="Age Wise Analysis")))
            ], className="col-md-6 mt-5"),
        ],className="row"),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dcc.Dropdown(id="picker",options=options,value="All"),
                        dcc.Graph(id="bar")
                    ],className="card-body")
                ],className="card")]
                , className="col-md-12 mt-5"),
],className="row")
    ],className="container")


@app.callback(Output("bar","figure"),[Input("picker","value")])
def update_graph(type):
    if type=="All":
        pbar = patients["detected_state"].value_counts().reset_index()
        return {
            "data": [go.Bar(x=pbar["detected_state"],y=pbar["count"])],
            "layout": go.Layout(title="State Wise Count")
        }
    else :
        npat=patients[patients["current_status"]==type]
        pbar = npat["detected_state"].value_counts().reset_index()
        return {
            "data": [go.Bar(x=pbar["detected_state"], y=pbar["count"])],
            "layout": go.Layout(title="State Wise Count")
        }

if __name__=="__main__":
    app.run_server(debug=True)