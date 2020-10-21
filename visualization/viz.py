import pandas as pd
import numpy as np
import dash                     #(version 1.0.0)
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import plotly.offline as py     #(version 4.4.1)
import plotly.graph_objs as go
import psycopg2 as pg
import pandas.io.sql as psql
import socket
import os
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

mapbox_access_token = open(".mapbox_token").read()


# Load the configuration for credentials
with open("config.json") as config_json:
    config = json.load(config_json)

# Connect to the database
engine = pg.connect(host = config['postgre']['ip'],
                             port = config['postgre']['port'],
                             database = config['postgre']['db'],
                             user = config['postgre']['user'],
                             password = config['postgre']['password'])

# Loading data with pgcursor then turning to pandas df
pgcursor = engine.cursor()
#-------------------------------------------------------
# Reading the data from database
sql_query = """select * from nearest_complaints"""
df = psql.read_sql(sql_query, engine)

sql_query = """select * from top_complaints"""
complaint_df = psql.read_sql(sql_query, engine)

sql_query = """select * from top_hours"""
hour_df = psql.read_sql(sql_query, engine)

df = df.merge(hour_df)
df = df.merge(complaint_df)

# Create new columns: month and year
df['year'] = pd.DatetimeIndex(df['created_date']).year
df['month'] = pd.DatetimeIndex(df['created_date']).month

# app_flask = Flask(__name__)
app = dash.Dash(__name__)

blackbold={'color':'black', 'font-weight': 'bold'}

# Import logo image
image_filename = 'Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([
#---------------------------------------------------------------
# Map_legen + Borough_checklist + Complaint_Checklist + Date Filtering +Web_link + Map
    html.Div([
        html.Div([
            # Map-legend
            # html.Ul([
            #     html.Li("Test", className='circle', style={'background': '#ff00ff','color':'black',
            #         'list-style':'none','text-indent': '17px'}),
            #     html.Li("Test1", className='circle', style={'background': '#0000ff','color':'black',
            #         'list-style':'none','text-indent': '17px','white-space':'nowrap'}),
            #     html.Li("Test2", className='circle', style={'background': '#FF0000','color':'black',
            #         'list-style':'none','text-indent': '17px'}),
            #     html.Li("Test3", className='circle', style={'background': '#00ff00','color':'black',
            #         'list-style':'none','text-indent': '17px'}),
            #     html.Li("Test4", className='circle',  style={'background': '#824100','color':'black',
            #         'list-style':'none','text-indent': '17px'}),
            # ], style={'border-bottom': 'solid 3px', 'border-color':'#00FC87','padding-top': '6px'}
            # ),

            # Borough_checklist
            html.Label(children=['Select borough to filter by: '], style=blackbold),
            dcc.Checklist(id='boro_name',
                    options=[{'label':str(b),'value':b} for b in sorted(df['neighbourhood_group_cleansed'].unique())],
                    value=[b for b in sorted(df['neighbourhood_group_cleansed'].unique())],
            ),

            # Neighborhood_checklist
            html.Label(children=['Select neighborhood to filter by: '], style=blackbold),
            dcc.Checklist(id='neigh_name',
                    options=[{'label':str(b),'value':b} for b in sorted(df['neighbourhood_cleansed'].unique())],
                    value=[b for b in sorted(df['neighbourhood_cleansed'].unique())],
            ),

            # complaint checklist
            html.Label(children=['Select complaint to filter by'], style=blackbold),
            dcc.Checklist(id='recycling_type',
                    options=[{'label':str(b),'value':b} for b in sorted(df['clean_complaint'].unique())],
                    value=['Noise'], #[b for b in sorted(df['top_complaint'].unique())]
            ),

            # Year checklist
            html.Label(children=['Select year to filter by'], style=blackbold),
            dcc.Checklist(id='year_type',
                    options=[{'label':str(b),'value':b} for b in sorted(df['year'].unique())],
                    value=[b for b in sorted(df['year'].unique())],
            ),

            # Month checklist
            html.Label(children=['Select month to filter by'], style=blackbold),
            dcc.Checklist(id='month_type',
                    options=[{'label':str(b),'value':b} for b in sorted(df['month'].unique())],
                    value=[b for b in sorted(df['month'].unique())],
            ),

            # Price checklist
            html.Label(children=['Select price range to filter by'], style=blackbold),
            dcc.Checklist(id='price_type',
                    options=[{'label':str(b),'value':b} for b in ['< $100', '> $100']],
                    value=[b for b in ['< $100', '> $100']],
            ),

            # Web_link
            html.Br(),
            html.Label(['Airbnb Listing Link:'],style=blackbold),
            html.Pre(id='web_link', children=[],
            style={'white-space': 'pre-wrap','word-break': 'break-all',
                 'border': '1px solid black','text-align': 'center',
                 'padding': '12px 12px 12px 12px', 'color':'blue',
                 'margin-top': '3px'}
            ),

        ], className='three columns'
        ),

        html.Div([
            html.Img(
                src='https://raw.githubusercontent.com/ednmolina/ABeautifulStayInTheNeighborhood/master/images/Logo.png',
                style={
                    'height' : '30%',
                    'width' : '30%',
                    'float' : 'center',
                    'position' : 'static',
                    'padding-top' : 0,
                    'padding-right' : 0
                })
    ]),

        # Map
        html.Div([
            dcc.Graph(id='graph', config={'displayModeBar': False, 'scrollZoom': True},
                style={'background':'#00FC87','padding-bottom':'2px','padding-left':'2px','height':'100vh'}
            )
        ], className='nine columns'
        ),

    ], className='row'
    ),

], className='ten columns offset-by-one'
)

#---------------------------------------------------------------
# Output of Graph
@app.callback(Output('graph', 'figure'),
              [Input('boro_name', 'value'),
              Input('neigh_name', 'value'),
              Input('recycling_type', 'value'),
              Input('year_type', 'value'),
              Input('month_type', 'value'),
              Input('price_type', 'value')])

def update_figure(chosen_boro,chosen_neighborhood, chosen_recycling,chosen_year, chosen_month, chosen_price):

    # if 'Lower East Side' in chosen_neighborhood:
    #     chosen_boro = chosen_boro.append(['Manhattan'])
    #     print (chosen_boro)

    df_sub = df[(df['neighbourhood_group_cleansed'].isin(chosen_boro)) &
                (df['neighbourhood_cleansed'].isin(chosen_neighborhood)) &
                (df['clean_complaint'].isin(chosen_recycling)) &
                (df['year'].isin(chosen_year)) &
                (df['month'].isin(chosen_month))]

    # Check if user has filtered for price range
    if chosen_price == ['< $100']:
        df_sub = df_sub[df_sub['price']<np.float(100.0)]
    elif chosen_price == ['> $100']:
        df_sub = df_sub[df_sub['price']>np.float(100.0)]
    else:
        df_sub = df_sub

    # Create hovertext by combining columns
    df_sub['hovtext'] = 'Bedrooms: '+df_sub['bedrooms'].astype(str)+'<br>'+'Bathrooms: '+df_sub['bathrooms'].astype(str)+\
    '<br>Price: $'+df_sub['price'].astype(str)+\
    '<br>Min Nights: '+df_sub['minimum_nights'].astype(str)+'<br>Number of Reviews: '+df_sub['number_of_reviews'].astype(str)+\
    '<br>When Complaints Mostly Occur: '+df_sub['hour'].astype(str)+'<br>Top Complaint: '+df_sub['clean_complaint'].astype(str)+\
    '<br>30 Day Avg Price: $'+df_sub['avg_30_price'].round(2).astype(str)

    # Create the map
    locations=[go.Scattermapbox(
                    lon = df_sub['long_list'],
                    lat = df_sub['lat_list'],
                    mode='markers',
                    marker={'color' : '#EF3D4A'},
                    unselected={'marker' : {'opacity':.25, 'size':15}},
                    selected={'marker' : {'opacity':1, 'size':15}},
                    hoverinfo='text',
                    hovertext=df_sub['hovtext'],
                    customdata=df_sub['listing_url']
    )]

    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision= 'foo', #preserves state of figure/map after callback activated
            clickmode= 'event+select',
            hovermode='closest',
            hoverdistance=2,
            # title=dict(text="Be Our Guest",font=dict(size=50, color='#EE3D4B')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                style='light',
                center=dict(
                    lat=df['lat_list'].mean(), #, -73.956661 df_sub['lat_list'].mean()
                    lon=df['long_list'].mean()
                ),
                pitch=0,
                zoom=14
            ),
        )
    }
#---------------------------------------------------------------
# callback for Web_link
@app.callback(
    Output('web_link', 'children'),
    [Input('graph', 'clickData')],
    )
def display_click_data(clickData):
    if clickData is None:
        return 'Click on any Airbnb on the map to get its listing url'
    else:
        # print (clickData)
        the_link=clickData['points'][0]['customdata']
        if the_link is None:
            return 'No Data Available'
        else:
            return html.A(the_link, href=the_link, target="_blank")

# #--------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=80, host=config["ec2"]["host"])
