import pandas as pd
import sqlite3
import requests
with open('com.txt') as f:
    companies = [line.strip() for line in f]
conn = sqlite3.connect('finance.db')
for company in companies:
    u = f'https://finance.yahoo.com/quote/{company}/history?p={company}'
    ul =  requests.get(u,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    df = pd.read_html(ul.text)[0]
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    df.to_sql(name='finance', con=conn, if_exists='append', index=False)
    
conn.close()
