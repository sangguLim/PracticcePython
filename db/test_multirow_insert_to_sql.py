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
        #sclt= con.execute(f"select * from alpha_platform.TEMP.DAYNAME").fetchall()
        #print(sclt)

        #data 추가
        # csv -> dataframe
        datedate= '20221024'
        PATH = 'D:\\Barra\\daily\\'
        FILE_NAME='USMEDS_100_UnadjCovariance' 
        CSV_NAME= FILE_NAME+'_'+datedate+'.csv'
        tbName= 'USMEDS_100_UnadjCovariance'
        DF_COL_NAME= '(''FACTOR1'',''FACTOR2'', ''VARCOVAR'', ''DATADATE'')'


        # 컬럼명 설정해서 불러오기
        data_result = pd.read_csv(PATH+CSV_NAME
                                    , sep=('|')
                                    ,header=0
                                    ,skiprows=2
                                    ,skipfooter=1
                                    , names = ['Id', 'FACTOR2', 'VARCOVAR','DATADATE']   # 대소문자 db 컬럼명과 맞춰줘야 함
                                    , engine='python')
        data_result['FACTOR1']= data_result.Id.str.split(',').str[1]            #Id 라는 컬럼에서 , 기준으로 split 후 FACTOR1이라는 새로운 컬럼 생성
        data_result=data_result[['FACTOR1','FACTOR2', 'VARCOVAR','DATADATE']]        
        print(data_result)#.head(10)    

        conn.execute('ALTER SESSION SET AUTOCOMMIT=TRUE')
        data_result.to_sql(tbName, con=conn, chunksize=1000, index=False, schema= 'BARRA', method=pd_writer, if_exists="append") 
        """
        # 행 추가 시 옵션 설정
        data_result.insert(0,'DATADATE',datedate)                 # csv파일에 쓰여있는 date기입, 0번째/컬럼명: 'datadate'/값: '20221216'


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
        # for idx,row in data_result.iterrows():
        #     conn.execute(qry,row.to_list())
        #     #conn.execute('COMMIT;')
        conn.execute('ALTER SESSION SET AUTOCOMMIT=TRUE')
        data_result.to_sql(tbName, con=conn, chunksize=1000, index=False, schema= 'BARRA', method=pd_writer, if_exists="append") 
        ##------------------------------------------------------------------------------------------

        #df = data_result[[col.name for col in table.columns]]

        #stage_table = f"{stage_prefix}_{table.name}"



        with self.connect() as con:

            df.to_sql(stage_table, if_exists="fail", con=con, index=False)

        self.merge_into_table(stage_table, table, comp_cols=comp_cols)

        with self.connect() as con:

            con.execute(f"DROP TABLE {stage_table}")
        """
        #con.execute(f"DROP TABLE {stage_table}")
        #pd.to_sql(stage_table, if_exists="fail", con=con, index=False)
    except Exception as e:
        print(e)
    finally:
        conn.close()

enddt= dt.datetime.now()

print("start time:\t",srtdt,"\nend time:\t",enddt,"\nexecute time:\t",enddt- srtdt)
# to_sql 사용해서 데이터 isnert
# data_result.to_sql(tbName, if_exists="fail", con=conn, index=False, schema= 'BARRA') 