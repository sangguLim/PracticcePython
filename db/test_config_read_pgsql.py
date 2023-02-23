import sys
import pandas as pd
sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connPg

conn= connPg.connPgdb('compustat_high')

sql = '''select * from public.daily_famafrench_factor limit 10;'''
result = pd.read_sql(sql,conn)
print(result)

conn.close()