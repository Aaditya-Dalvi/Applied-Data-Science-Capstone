import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State

app=dash.Dash(__name__)
auto_data =  pd.read_csv('automobileEDA.csv', 
                            encoding = "ISO-8859-1",
                            )

app.layout=html.Div(children=[
    html.H1('Car Automobile Components', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 24}),
    html.H2('Drive Wheels Type:', style={'margin-right': '2em'}),

    #Outer Division starts
    html.Div(children[

        #inner division 1
        html.Div(
             dcc.Dropdown(id="demo-dropdown",
        options=[
            {'label':'Rear Wheel Drive','value':'rwd'},
            {'label':'Front Wheel Drive','value':'fwd'},
            {'label':'Four Wheel Drive','value':'4wd'}
                ],value='rwd')
                ),

        #inner division 2
        html.Div([
            html.Div([],id='plot1'),
            html.Div([],id='plot2')

        ],style={'display':'flex'}
        ) 
    ])

])

@app.callback([Output(component_id='plot1',component_property='children'),
               Output(component_id="plot2",component_property='children')],
               Input(component_id='demo-dropdown',component_property='value')
)

def display_selected_drive_charts(value):
   

   
   filtered_df = auto_data[auto_data['drive-wheels']==value].groupby(['drive-wheels','body-style'],as_index=False). \
            mean()
        
   filtered_df = filtered_df
   
   fig1 = px.pie(filtered_df, values='price', names='body-style', title="Pie Chart")
   fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')
    
   return [dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2) ]


if __name__=="__main__":
    app.run_server(debug=True)