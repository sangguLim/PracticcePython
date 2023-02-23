from __future__ import annotations

import datetime as dt
import pandas as pd
import sys
#from glue.snowflake import Snowflake
from snowflake.connector.pandas_tools import write_pandas, pd_writer
# snowflake 커넥션
sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon

sf= sfcon.sf()

# 시작 시간 설정 (로그용)
srtdt = dt.datetime.now()

with sf.connect() as conn:
    try:
        conn.execute(f"USE SCHEMA BARRA")
        
        # csv -> dataframe
        datedate= '20221216'
        PATH = 'D:\\Barra\\daily\\'
        CSV_NAME= 'USA_XSEDOL_Asset_ID_'+datedate+'.csv'
        tbName= 'USA_XSEDOL_Asset_ID'
        DF_COL_NAME= '(''DATADATE'',''BARRAID'', ''ASSETIDTYPE'', ''ASSETID'',''STARTDATE'',''ENDDATE'')'

        # 컬럼명 설정해서 불러오기
        data_result = pd.read_csv(PATH+CSV_NAME
                                    , sep=('|')
                                    ,header=0
                                    ,skiprows=1
                                    ,skipfooter=1
                                    , names = ['Id', 'ASSETIDTYPE', 'ASSETID','STARTDATE','ENDDATE']   # 대소문자 db 컬럼명과 맞춰줘야 함
                                    , engine='python')
        # 행 추가 시 옵션 설정
        data_result.insert(0,'DATADATE',datedate)                 # csv파일에 쓰여있는 date기입, 0번째/컬럼명: 'datadate'/값: '20221216'

        data_result['BARRAID']= data_result.Id.str.split(',').str[1]

        data_result=data_result[['DATADATE','BARRAID','ASSETIDTYPE','ASSETID','STARTDATE','ENDDATE']]        
        
        data_result= data_result.head(1000)

        #con.execute(f"insert into {TBL_NAME} values[{df_list}]")
        
        # 인서트 쿼리문
        # for i in data_result:
        #     con.execute(f"insert into {TBL_NAME}values{i}")
        qry='''
            insert into ''' + tbName + '''
                        ''' + DF_COL_NAME + '''
            values(%s,%s,%s,%s,%s,%s)
        '''
        #print(qry)
        for idx,row in data_result.iterrows():
            conn.execute(qry,row.to_list())
            #conn.execute('COMMIT;')
        #data_result.to_sql(tbName, con=conn, chunksize=1000, index=False, schema= 'BARRA', method=pd_writer, if_exists="append") 
        
        
        #con.execute(f"DROP TABLE {stage_table}")
        #pd.to_sql(stage_table, if_exists="fail", con=con, index=False)
    except Exception as e:
        print(e)
enddt= dt.datetime.now()

print("start time:\t",srtdt,"\nend time:\t",enddt,"\nexecute time:\t",enddt- srtdt)
# to_sql 사용해서 데이터 isnert
# data_result.to_sql(tbName, if_exists="fail", con=conn, index=False, schema= 'BARRA') 