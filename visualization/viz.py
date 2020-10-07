import dash
import dash_core_components as dcc
import dash_html_components as html

# Load the configuration for credentials
with open("config.json") as config_json:
    config = json.load(config_json)

# Connect to the database
pgconnect = psycopg2.connect(host = config['postgre']['ip'],
                             port = config['postgre']['port'],
                             database = config['postgre']['db'],
                             user = config['postgre']['user'],
                             password = config['postgre']['password'])

pgcursor = pgconnect.cursor()
