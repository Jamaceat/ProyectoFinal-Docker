import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import plotly.graph_objs as go
import plotly.express as px

conn = psycopg2.connect("postgresql://postgres:postgres@db")  
cursor = conn.cursor()
df1 = sqlio.read_sql_query('SELECT payment_date,amount FROM payment LIMIT 10',conn)
df2 = sqlio.read_sql_query('SELECT COUNT(c.*) AS numcustomer,ct.city FROM customer AS c \
                    INNER JOIN address AS a ON c.address_id=a.address_id \
                    INNER JOIN city AS ct ON a.city_id=ct.city_id GROUP BY ct.city_id LIMIT 25',conn)
df3 = sqlio.read_sql_query('SELECT COUNT(f.title) AS numfilms,f.rating FROM film AS f GROUP BY f.rating',conn)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data1 = px.bar(x=df1.payment_date, y=df1.amount,title='Valor de pagos por fecha')
data2 = px.pie(df2, values='numcustomer',names='city',title='Clientes por ciudad')
data3 = px.bar(x=df3.numfilms,y=df3.rating,orientation='h',title='Num. películas por clasificación')


app.layout = html.Div(children=[
    html.H1(children='G3 - Proyecto Final PC2',style={'textalign':'center'}),

    dcc.Graph(
        id='Graph1',
        figure=data1
    ),

    dcc.Graph(
        id='Graph2',
        figure=data2
    ),

    dcc.Graph(
        id='Graph3',
        figure=data3
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)