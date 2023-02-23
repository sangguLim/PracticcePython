import sys
from pathlib import Path
import pandas as pd
import datetime as dt

sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connTeams
import connSnowflake as sfcon

sf= sfcon.sf()

with sf.connect() as conn:
    try:
        date= dt.datetime.now().strftime('%Y-%m-%d')
        conn.execute("USE SCHEMA PUBLIC")
        qry= f'''
            select case when USA_HLD=1 then 'Holiday' else 'OpenDay' end as holiday_yn 
            from date
            where date= '{date}'
        '''
        holiday=pd.read_sql(qry,conn)
        holiday= holiday['holiday_yn'].values.tolist()

        #holiday= 
        if holiday[0]=='OpenDay':
            print('Open')
        else:
            print('Close')
        #print(holiday)
    except Exception as e:
        print(e)
    finally:
        conn.close()
        