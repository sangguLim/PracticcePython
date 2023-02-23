# ------------------------------------------------------------------------------ #
# 파일명   :   test_pickle
# 작성자   :   sanggu.lim
# 작성일   :   2023년 2월 15일
# 작성목적 :   Test Message Send to Mailing
# ------------------------------------------------------------------------------ #

import pickle

from alphaju import get_factor_data
import pandas as pd
import sys
import sqlalchemy
import datetime as dt

sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon

from snowflake.connector.pandas_tools import pd_writer
sf=sfcon.sf()



# save
# with open('factor_list.pkl', 'wb') as f:
#     pickle.dump(df, f, pickle.HIGHEST_PROTOCOL)


## pkl파일 호출 단계
with open('factor_list.pkl', 'rb') as f:
    df = pickle.load(f)

df=df.rename(columns={"fac_no":"FAC_NO","directory":"DIRECTORY","factor_name":"FACTOR_NAME","use_yn":"USE_YN"})
print(df)
print(df.info())
        
## db 인서트 단계
with sf.connect() as conn:
    try:        
        conn.execute("USE SCHEMA PUBLIC")        
        
        # data_result=pd.DataFrame({
        #     "DATE": dt.datetime.now(),
        #     "FACTOR" : factorName,
        #     "ERROR_COMMENT": errorCmt
        # })
        #df=df.reset_index()
        #print(df.columns)
        tbName= "temp_pkl_tbl"

        conn.execute('ALTER SESSION SET AUTOCOMMIT=TRUE')
        df.to_sql(tbName,
                conn,
                index= False,
                #index_label= "fac_no",
                schema="TEMP",
                method= pd_writer,
                if_exists="replace"
                )
    except Exception as e:
        print(e)
    finally:
        conn.close()