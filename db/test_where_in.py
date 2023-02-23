from alphaju import get_factor_data
import pandas as pd
import sys
import sqlalchemy
import datetime as dt

sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon
import connTeams
from snowflake.connector.pandas_tools import pd_writer

sf= sfcon.sf()

with sf.connect() as conn:
    try:
        conn.execute(f"USE SCHEMA PUBLIC")

        where_condition= ('001690','322996')
        where_condition_list= list(where_condition)
        sql='''
            select distinct 
                gvkey,
                iid
            from public.sec_meta
            where gvkey in {}
        '''
        print(sql.format(where_condition))
        #qry_result= conn.execute(sql.format(where_condition))
        qry_result= pd.read_sql(sql.format(where_condition),conn)
        #qry_result= cursor.sql(sql.format(where_condition)).collect()
        print(qry_result)
    except Exception as e:
        print(e)
    finally:
        conn.close()