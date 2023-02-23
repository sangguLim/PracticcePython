from alphaju import get_factor_data
import pandas as pd
from pandas import pivot
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
        conn.execute("USE SCHEMA PUBLIC")
        
        qry= '''
            select distinct factor
            from public.factor_longform;
        '''
        factor_read= pd.read_sql(qry,conn)
        #print("factor_cnt:\t",factor_cnt)
        srtTime= dt.datetime.now()

        print(factor_read)

        factor_list=[]

        # 데이터프레임 중 원하는 컬럼을 리스트화
        for idx in factor_read.index:
            print(factor_read.loc[idx,'factor']) #factor 자리에 컬럼명 기입

        # for i,row in factor_read.iterrows():
        #     # factor_list.append(i)
        #     print(i)
        #     print(row)
            
        
        #print(factor_list)
        # for i in factor_list:
        #     qry= f'''
        #         select *
        #         from public.factor_longform
        #         where factor in ({i})
        #         ;
        #     '''
        #     print(qry)

        # df= pd.read_sql(qry,conn)
        # endTime= dt.datetime.now()
        # print("data read:\t",endTime-srtTime)

        # # 2개 : 
        # # 3개 : 
        # # 4개 : 0:02:20.732078

        # srtTime= dt.datetime.now()
        # df= df.pivot(["datadate","gvkeyiid"],"factor","value")
        # df= df.reset_index()

        # # 2개 : 0:01:11.842151
        # # 3개 : 0:02:00.765994
        # # 4개 : 

        # print(df)
        # endTime= dt.datetime.now()
        # print("pivot:\t",endTime-srtTime)
        # instbName= (f"public.factor")
        




        #for i in 
        #pd.merge(left = df , right = df, how = "inner", on = "이름")

        # df.to_sql(instbName,
        #             con= conn,
        #             chunksize= 1000000,
        #             index=False,
        #             schema="PUBLIC",
        #             method= pd_writer,
        #             if_exists="replace",  #append, fail
        #             )
    except Exception as e:
        print(e)
    finally:
        conn.close()
