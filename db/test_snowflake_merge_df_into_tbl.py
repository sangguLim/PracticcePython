import json
import datetime as dt
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,TIMESTAMP
from snowflake.sqlalchemy import URL
import snowflake.connector as  sc
from pathlib import Path
#import sys
#sys.path.append('C:\\Users\\USER\\Documents\\glue')

from glue.snowflake import Snowflake
meta = MetaData()
ACCOUNT_FP = "C:\\Users\\USER\\Documents\\alphaplatform-db\\etf_migration\\snowflake_update\\snowflake_account.json"
#ACCOUNT_FP = f"{Path.cwd().as_posix()}\\etf_migration\\snowflake_update\\snowflake_account.json"

with open(ACCOUNT_FP, "r") as f:
            account_info = json.load(f)
engine = create_engine(URL(**account_info))
conn = engine.connect()
#sfcur = sc.cursor()

try:
    # 단일행 인서트쿼리문 
    # insert_list=('2022-12-26', 1)
    # insertExec = conn.execute("insert into alpha_platform.temp.test_table(DATA_DATE,USL_HLD) "
    #                             " VALUES (%s,%s)"
    #                             ,insert_list).fetchone()
    
    #success
        ## insertExec = conn.execute("insert into alpha_platform.temp.test_table(DATA_DATE,USL_HLD) "
                                # " VALUES (%s,%s)"
                                # ,insert_list).fetchone()    
        ## insertExec = conn.execute("insert into alpha_platform.temp.test_table(DATA_DATE,USL_HLD) VALUES('2022-12-26', 1);").fetchone()
    insert_table= Table(
        'alpha_platform.temp.test_table',   # db 내 저장될 table name
        meta,
        Column('data_date',TIMESTAMP,primary_key=True), # 이 테이블에 들어갈 컬럼입니다
        Column('usl_hld',Integer)
    )
    
    insert_list= [('2022-12-26', 1),('2022-12-27', 2)]
    insert_df= pd.DataFrame(insert_list)
    #insert_tbl= 'alpha_platform.temp.test_table'
    comp_col= ('DATA_DATE','USL_HLD')
    #insertExec = sc.cursor().executemany("insert into alpha_platform.temp.test_table(DATA_DATE,USL_HLD) VALUES(?,?)",insert_list)
    Snowflake.merge_dataframe_into_table(insert_df, insert_table, comp_col)
    # 조회쿼리문
    #results = conn.execute("select PriceIndex, TotalIndex, NetIndex from alpha_platform.public.port_index where portid='qrft2' and datadate='2022-11-25';").fetchone()
    #print(results)
finally:
    conn.close()
    engine.dispose()

'''
def getSFopen(dbname): # where 조건절에 들어갈 컬럼값 설정
    if dbname =='alpha':
        with open(ACCOUNT_FP, "r") as f:
            account_info = json.load(f)
        # sf = Snowflake(
        # role='alpha_platform',
        # warehouse='COMPUTE_WH',
        # user='sanggu.lim',
        # password='Dlatkdrn95!')
        conn = create_engine(URL(**account_info))
    return conn
    #IDF_meta = pd.read_csv('./meta.csv')

def init_connection_engine(
    cloudsql_prn, cloudsql_connstring
) -> sqlalchemy.engine.Engine:
    def get_dbname(url):
        return re.match(".*dbname='(.*?)'", url).groups()[0]

    def get_user(url):
        return re.match(".*user='(.*?)'", url).groups()[0]

    def get_password(url):
        return re.match(".*password='(.*?)'", url).groups()[0]

    def getconn() -> pg8000.dbapi.Connection:
        return connector.connect(
            instance_connection_string=cloudsql_prn,
            driver="pg8000",
            user=get_user(cloudsql_connstring),
            password=get_password(cloudsql_connstring),
            db=get_dbname(cloudsql_connstring),
        )

    engine = sqlalchemy.create_engine("postgresql+pg8000://", creator=getconn)
    engine.dialect.description_encoding = None
    return engine
    
    '''