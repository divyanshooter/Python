import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc,dash


data=pd.read_csv('gapminder.csv')

# print(data.columns)

app=dash.Dash()
app.layout= html.Div([
    html.Div(children=[
        html.H1(children="Gapminder Dashboard",style={'color':'red','text-align':'center','margin':'auto'})
        ]
,style={'border':'1px solid black','float':'left','width':'100%','height':'50px'}),
    html.Div(children=[
        dcc.Graph(id='scatter_plot',figure={'data':[go.Scatter(x=data['pop'],y=data['gdpPercap'],mode='markers')],
                                            'layout':go.Layout(title='Population Vs GDP',xaxis={'title':'Population'},yaxis={'title':'GDP Per Capita'})})
    ],style={'border':'1px solid black','float':'left','width':'49.8%','height':'450px'}),
    html.Div(children=[
        dcc.Graph(id='box_plot',figure={'data':[go.Box(x=data['gdpPercap'],name='GDP')],'layout':go.Layout(title='Box plot')})
    ],style={'border':'1px solid black','float':'left','width':'49.8%','height':'450px'})
])

if __name__=='__main__':
    app.run()

