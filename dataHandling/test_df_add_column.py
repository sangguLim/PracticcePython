import pandas as pd
import sys
import pickle
sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon

from snowflake.connector.pandas_tools import pd_writer
sf= sfcon.sf()

# with sf.connect() as conn:
#     conn.execute("USE SCHEMA PUBLIC")
#     ## pkl파일 호출 단계
#     with open('factor_frame.pkl', 'rb') as f:
#         df = pickle.load(f)
        
#     conn.close()
# df['value'] =  float('nan')

with sf.connect() as conn:
    conn.execute("USE SCHEMA PUBLIC")
    
    tbName= "factor_longform_recalculate"
    qry= f'''
            select datadate,gvkeyiid,value
            from {tbName}
            where factor ='Dollar_Volume_1M'
                and value is not null;            
        '''
    factor_read= pd.read_sql(qry,conn)
    print(factor_read)
    #merged= pd.merge(df,factor_read,on=['datadate','gvkeyiid'],how= 'left')
    #print(merged)
    conn.close()
# 

# # 새로운 DataFrame 생성
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# # 'C'라는 이름의 새로운 열 추가
# df['C'] =None
# with sf.connect() as conn:
#     conn.execute("USE SCHEMA PUBLIC")
#     instbName="test_df_none"
#     conn.execute('ALTER SESSION SET AUTOCOMMIT=TRUE')
#     df.to_sql(instbName,
#                     con= conn,
#                     index=False,
#                     schema="TEMP",
#                     method= pd_writer,
#                     if_exists="replace"  #append, fail)
#     )
#     conn.close()
