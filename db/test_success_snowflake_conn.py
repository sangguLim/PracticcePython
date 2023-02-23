import json
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
import re
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

#import sys
#sys.path.append('C:\\Users\\USER\\Documents\\glue')

from glue.snowflake import Snowflake

ACCOUNT_FP = "C:\\Users\\USER\\Documents\\alphaplatform-db\\etf_migration\\snowflake_update\\snowflake_account.json"

with open(ACCOUNT_FP, "r") as f:
            account_info = json.load(f)
engine = create_engine(URL(**account_info))
try:
    connection = engine.connect()
    results = connection.execute("select PriceIndex, TotalIndex, NetIndex from alpha_platform.public.port_index where portid='qrft2' and datadate='2022-11-25';").fetchone()
    print(results)
finally:
    connection.close()
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