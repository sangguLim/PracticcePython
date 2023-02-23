from __future__ import annotations
import os
import datetime as dt
import pandas as pd
import sys
import warnings
import sqlalchemy
from snowflake.connector.pandas_tools import write_pandas, pd_writer

# snowflake 커넥션
sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon

sf= sfcon.sf()


with sf.connect() as conn:
    try:
        # 경고 문구 끄기
        warnings.filterwarnings(action='ignore')
        conn.execute(f"USE SCHEMA BARRA")
        # csv -> dataframe
        datedate= '20221223'
        #datedate= (dt.datetime.now()+dt.timedelta(days=-1)).strftime('%Y%m%d') 
        datedate_YYYYMMDD= dt.datetime.strptime(datedate, '%Y%m%d').strftime('%Y-%m-%d')
        PATH = 'D:\\Barra\\daily\\'
        FILE_NAME='FP_USMEDS_Factor_POR' 
        CSV_NAME= FILE_NAME+'_'+datedate+'.csv'
        tbName= 'LOGGING_TEST'

        # 컬럼명 설정해서 불러오기
        data_result = pd.read_csv(PATH+CSV_NAME
                                    , sep=('|')
                                    ,header=0
                                    ,skiprows=2
                                    ,skipfooter=1
                                    , names = ['Id','FACTOR','WEIGHT']   # 대소문자 db 컬럼명과 맞춰줘야 함
                                    , engine='python')
        data_result['BARRAID']= data_result.Id.str.split(',').str[1]            #Id 라는 컬럼에서 , 기준으로 split 후 FACTOR1이라는 새로운 컬럼 생성
        data_result=data_result.drop(['Id'],axis='columns')
        #print(data_result)#.head(10)    
        # 행 추가 시 옵션 설정
        data_result.insert(0,'DATADATE',datedate_YYYYMMDD)
        data_result=data_result[['BARRAID','FACTOR','WEIGHT','DATADATE']]    
        data_result=data_result.head(1004)
        conn.execute('ALTER SESSION SET AUTOCOMMIT=TRUE')
        data_result.to_sql(tbName, 
                            con=conn, 
                            chunksize=1000, 
                            index=False, 
                            schema= 'BARRA', 
                            method=pd_writer, 
                            if_exists="append",
                            dtype={
                                'BARRAID': sqlalchemy.types.VARCHAR(20),
                                'FACTOR': sqlalchemy.types.VARCHAR(20),
                                'WEIGHT': sqlalchemy.types.FLOAT,
                                'DATADATE': sqlalchemy.types.DateTime()
                                }) 
        
        conn.execute('''insert into alpha_platform.public.exec_log
                                (
                                    exec_date,
                                    proc_name,
                                    tgt_tbl_name,

                                ) 
                    values()''')
    except Exception as e:
        print(e)
    finally:
        conn.close()
        # 다시 출력하게 하기
        warnings.filterwarnings(action='default')

enddt= dt.datetime.now()

time_comment= "end time:\t"+str(enddt)+"\nexecute time:\t"+str(enddt- srtdt)+"\n"
len_comment= "data_cnt:\t"+str(len(data_result))
print(time_comment,len_comment)