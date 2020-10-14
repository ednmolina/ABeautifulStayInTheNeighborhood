# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd
# import pandas.io.sql as psql
# import json
# import psycopg2 as pg
# import plotly.graph_objects as go
# # from app import server
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# mapbox_access_token = open(".mapbox_token").read()
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# # Load the configuration for credentials
# with open("config.json") as config_json:
#     config = json.load(config_json)
#
# # Connect to the database
# engine = pg.connect(host = config['postgre']['ip'],
#                              port = config['postgre']['port'],
#                              database = config['postgre']['db'],
#                              user = config['postgre']['user'],
#                              password = config['postgre']['password'])
#
# # Loading data with pgcursor then turning to pandas df
# # pgcursor = engine.cursor()
#
# # pgcursor.execute("""
# #                  select
# #                      c.created_date,
# #                      c.clean_complaint,
# #                      c.complaint_type,
# #                      c.incident_zip,
# #                  	l.listing_id,
# #                      l.latitude lat_list,
# #                      l.longitude long_list,
# #                  	l.price,
# #                  	l.bedrooms,
# #                  	l.bathrooms,
# #                  	l.avg_30_price,
# #                  	l.minimum_nights,
# #                  	l.neighbourhood_cleansed
# #                  from filtered_complaints c, listings l
# #                  where ST_Intersects(c.circle, l.circle) limit 1000""")
# #
# # df = pgcursor.fetchall()
# # db_df = pd.DataFrame(df)
# # print (db_df)
#
# # Reading data directly from database using pandas
# # sql_query = """
# #                  select
# #                      c.created_date,
# #                      c.clean_complaint,
# #                      c.complaint_type,
# #                      c.incident_zip,
# #                  	l.listing_id,
# #                      l.latitude lat_list,
# #                      l.longitude long_list,
# #                  	l.price,
# #                  	l.bedrooms,
# #                  	l.bathrooms,
# #                  	l.avg_30_price,
# #                  	l.minimum_nights,
# #                  	l.neighbourhood_cleansed
# #                  from filtered_complaints c, listings l
# #                  where ST_Intersects(c.circle, l.circle) limit 50"""
# sql_query = """select * from nearest_complaints_test"""
# db_df = psql.read_sql(sql_query, engine)
#
# print (db_df)
# # Group the data by listing_id and determine; sort_values column can be anything since all columns contain count
# # This works for getting top complaint for each
# # db_df_grouped = db_df.groupby(['listing_id','clean_complaint'])['complaint_type'].agg(pd.Series.mode).to_frame()
#
# # print (db_df[['listing_id', 'clean_complaint', 'created_date', 'complaint_type']].groupby(['listing_id', 'clean_complaint']).size().groupby(level = 1).nlargest(3).reset_index(-1, drop=True))
#
# # print (db_df_grouped)
# # For each
# # # df = pd.DataFrame({
# # #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
# # #     "Amount": [4, 1, 2, 2, 4, 5],
# # #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# # # })
# # #
# # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
#
# # app.layout = html.Div(children=[
# #     html.H1(children='Hello Dash'),
# #
# #     html.Div(children='''
# #         Dash: A web application framework for Python.
# #     '''),
# #
# #     dcc.Graph(
# #         id='example-graph',
# #         figure=fig
# #     )
# # ])
# #
# site_lat = db_df['lat_list']
# site_lon = db_df['long_list']
# locations_name = db_df['price']
#
# fig = go.Figure(go.Scattermapbox(
#         lat=site_lat,
#         lon=site_lon,
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=9
#         ),
#         text=locations_name,
#     ))
#
#
# fig.update_layout(
#     title='Test Map',
#     autosize=True,
#     hovermode='closest',
#     showlegend=False,
#     mapbox=dict(
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#             lat=site_lat.mean(),
#             lon=site_lon.mean()
#         ),
#         pitch=0,
#         zoom=10,
#         style='light'
#     ),
#     height = 800
# )
#
# fig.show()
#
# blackbold={'color':'black', 'font-weight': 'bold'}
#
# app.layout = html.Div([
#     # Borough_checklist
#             html.Label(children=['Select a borough to search through: '], style=blackbold),
#             dcc.Checklist(id='boro_name',
#                     options=[{'label':str(b),'value':b} for b in sorted(['Manhattan', 'Brooklyn', 'Queens', 'Staten', 'Bronx'])],
#                     value=['Brooklyn'],#[b for b in sorted(['Manhattan', 'Brooklyn', 'Queens', 'Staten', 'Bronx'])]
#             ),
#
#             html.Div([
#             dcc.Graph( id='graph', config={'displayModeBar': False, 'scrollZoom': True}, #figure=fig,
#             )
#             ], #  className=' nine columns'
#             ),
#
# ],
# )
#
# #---------------------------------------------------------------
# # Callback what connects between user selection and figure that results
# # Output of Graph
# @app.callback(Output('graph', 'figure'),
#               [Input('boro_name', 'value'),
#                ])
# def update_figure(chosen_boro,chosen_recycling):
#     df_sub = df[(db_df['neighbourhood_group_cleansed'].isin(chosen_boro)) ]
#
#     # Create figure
#     locations=[go.Scattermapbox(
#                     lon = site_long,
#                     lat = site_lat,
#                     mode='markers',
#                     # marker={'color' : df_sub['color']},
#                     unselected={'marker' : {'opacity':1}},
#                     selected={'marker' : {'opacity':0.5, 'size':25}},
#                     hoverinfo='text',
#                     hovertext=df_sub['price'],
#                     # customdata=df_sub['website']
#     )]
#
#     #  Return figure
#     return {
#         'data': locations,
#         'layout': go.Layout(
#             uirevision= 'foo', #preserves state of figure/map after callback activated
#             clickmode= 'event+select',
#             hovermode='closest',
#             hoverdistance=2,
#             title=dict(text="Airbnb Listings for NYC with 311 complaint data",font=dict(size=50, color='red')),
#             mapbox=dict(
#                 accesstoken=mapbox_access_token,
#                 bearing=25,
#                 style='light',
#                 center=dict(
#                     lat=40.80105,
#                     lon=-73.945155
#                 ),
#                 pitch=40,
#                 zoom=11.5
#             ),
#         )
#     }
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050, host="ec2-18-144-167-237.us-west-1.compute.amazonaws.com")

""" Map 1 """
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.express as px
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
#
# # Data
# df = px.data.gapminder().query("year==2007")
#
# df = df.rename(columns=dict(pop="Population",
#                             gdpPercap="GDP per Capita",
#                             lifeExp="Life Expectancy"))
#
# cols_dd = ["Population", "GDP per Capita", "Life Expectancy"]
#
# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Dropdown(
#         id='demo-dropdown',
#         options=[{'label': k, 'value': k} for k in cols_dd],
#         value=cols_dd[0]
#     ),
#
#     html.Hr(),
#     dcc.Graph(id='display-selected-values'),
#
# ])
#
# @app.callback(
#     dash.dependencies.Output('display-selected-values', 'figure'),
#     [dash.dependencies.Input('demo-dropdown', 'value')])
#
# def update_output(value):
#     fig = go.Figure()
#     fig.add_trace(go.Choropleth(
#        locations=df['iso_alpha'], # Spatial coordinates
#         z=df[value].astype(float), # Data to be color-coded
#         colorbar_title=value))
#     fig.update_layout(title=f"<b>{value}</b>", title_x=0.5)
#     return fig
#
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050, host="ec2-18-144-167-237.us-west-1.compute.amazonaws.com")

"""MAP Checkbox test"""

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


df = df.merge(complaint_df)
df = df.merge(hour_df)

# Create new columns: month and year
df['year'] = pd.DatetimeIndex(df['created_date']).year
df['month'] = pd.DatetimeIndex(df['created_date']).month

# app_flask = Flask(__name__)
app = dash.Dash(__name__)

blackbold={'color':'black', 'font-weight': 'bold'}

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
            html.Label(children=['Select borough to filterby: '], style=blackbold),
            dcc.Checklist(id='boro_name',
                    options=[{'label':str(b),'value':b} for b in sorted(df['neighbourhood_group_cleansed'].unique())],
                    value=['Brooklyn'],
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
              Input('recycling_type', 'value'),
              Input('year_type', 'value'),
              Input('month_type', 'value')])

def update_figure(chosen_boro, chosen_recycling,chosen_year, chosen_month):
    df_sub = df[(df['neighbourhood_group_cleansed'].isin(chosen_boro)) &
                (df['clean_complaint'].isin(chosen_recycling)) &
                (df['year'].isin(chosen_year)) &
                (df['month'].isin(chosen_month))]
    # Need to group by listing id then get top complaints
    # print ("THIS IS DF_SUB")
    # print (df_sub)
    # print ("THIS IS SUB LAT LONG")
    # print (df_sub[['long_list', 'lat_list']])
    # Create figure
    # Create hovertext by combining columns
    df_sub['hovtext'] = 'Bedrooms: '+df_sub['bedrooms'].astype(str)+'<br>'+'Bathrooms: '+df_sub['bathrooms'].astype(str)+\
    '<br>Price: $'+df_sub['price'].astype(str)+\
    '<br>Min Nights: '+df_sub['minimum_nights'].astype(str)+'<br>Number of Reviews: '+df_sub['number_of_reviews'].astype(str)+\
    '<br>When Complaints Mostly Occur: '+df_sub['hour'].astype(str)+'<br>Top Complaint: '+df_sub['clean_complaint'].astype(str)+\
    '<br>30 Day Avg Price: $'+df_sub['avg_30_price'].round(2).astype(str)

    locations=[go.Scattermapbox(
                    lon = df_sub['long_list'],
                    lat = df_sub['lat_list'],
                    mode='markers',
                    marker={'color' : '#EF3D4A'},
                    unselected={'marker' : {'opacity':1, 'size':15}},
                    selected={'marker' : {'opacity':0.25, 'size':25}},
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
            title=dict(text="Be Our Guest",font=dict(size=50, color='red')),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                style='light',
                center=dict(
                    lat=np.float(40.711365), #, -73.956661 df_sub['lat_list'].mean()
                    lon=np.float(-73.954414)
                ),
                pitch=0,
                zoom=13
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
        return 'Click on any location'
    else:
        # print (clickData)
        the_link=clickData['points'][0]['customdata']
        if the_link is None:
            return 'No Data Available'
        else:
            return html.A(the_link, href=the_link, target="_blank")

# #--------------------------------------------------------------
if __name__ == '__main__':
    # Running the app
    # app.run_server(debug=True, host=host, port = 80)
    app.run_server(debug=True, port=80, host="ec2-54-193-212-80.us-west-1.compute.amazonaws.com")
    # app.run_server(debug=True, host="0.0.0.0", port = 80)
    # app_dash.run_server(debug = True)
    # app.run_server(debug=True, port=80, host="13.52.128.45")
