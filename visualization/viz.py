# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd
# import json
# import psycopg2
# import plotly.graph_objects as go
# # from app import server
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# mapbox_access_token = open(".mapbox_token").read()
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.config.suppress_callback_exceptions = True
#
# # Load the configuration for credentials
# with open("config.json") as config_json:
#     config = json.load(config_json)
#
# # Connect to the database
# pgconnect = psycopg2.connect(host = config['postgre']['ip'],
#                              port = config['postgre']['port'],
#                              database = config['postgre']['db'],
#                              user = config['postgre']['user'],
#                              password = config['postgre']['password'])
#
# pgcursor = pgconnect.cursor()
# # pgcursor.execute("""select c.complaint_type , c.created_date,  c.descriptor,
# #                       clean_complaint, c.month, c.year, l.listing_id, l.timestamp,
# # 		      l.price, l.longitude, l.latitude
# #                from listings as l
# #                cross join lateral( select *
# #                                    from complaints
# #                                    where (ST_Distance(complaints.geom, l.geom) < 100
# # 				  and created_date > '2018-01-01'
# # 				  and created_date < '2018-02-01')
# #                                    order by created_date limit 1) as c limit 20;""")
#
# pgcursor.execute("""select * from listings limit 20""")
#
# df = pgcursor.fetchall()
# db_df = pd.DataFrame(df)
# print (db_df)
#
# # df = pd.DataFrame({
# #     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
# #     "Amount": [4, 1, 2, 2, 4, 5],
# #     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# # })
# #
# # fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# #
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
# lat = db_df[1]
# long = db_df[2]
# text_data = db_df[5]
# fig = go.Figure(go.Scattermapbox(
#         lat=lat,
#         lon=long,
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=9
#         ),
#         textv = db_df[5]
#     ))
#
# fig.update_layout(
#     autosize=True,
#     hovermode='closest',
#     mapbox=dict(
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#             lat=lat.mean(),
#             lon=long.mean()
#         ),
#         pitch=0,
#         zoom=10
#     ),
#     height = 800
#
# )
#
# fig.show()
#
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8050, host="ec2-18-144-167-237.us-west-1.compute.amazonaws.com")

# save this as app.py
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Data
df = px.data.gapminder().query("year==2007")

df = df.rename(columns=dict(pop="Population",
                            gdpPercap="GDP per Capita",
                            lifeExp="Life Expectancy"))

cols_dd = ["Population", "GDP per Capita", "Life Expectancy"]

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{'label': k, 'value': k} for k in cols_dd],
        value=cols_dd[0]
    ),

    html.Hr(),
    dcc.Graph(id='display-selected-values'),

])

@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])

def update_output(value):
    fig = go.Figure()
    fig.add_trace(go.Choropleth(
       locations=df['iso_alpha'], # Spatial coordinates
        z=df[value].astype(float), # Data to be color-coded
        colorbar_title=value))
    fig.update_layout(title=f"<b>{value}</b>", title_x=0.5)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host="ec2-18-144-167-237.us-west-1.compute.amazonaws.com")
