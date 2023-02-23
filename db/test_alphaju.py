from alphaju import get_factor_data
import pandas as pd
import sys
import sqlalchemy
import datetime as dt

sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon
import connTeams
from snowflake.connector.pandas_tools import pd_writer

# 시작 시간 설정 (로그용)
srtdt = dt.datetime.now()
print("start time:\t",str(srtdt))

sf= sfcon.sf()
WebHook= connTeams.webhook()
myTeamsMessage = connTeams.pymsteams.connectorcard(WebHook)

tbName= 'factor_longform'
factor_name = 'Robust_Growth'


df = get_factor_data(factor_name,freq= "A")
print(df)
df_col_name = df.columns
print(df_col_name)
df= df.reset_index()
df_melt= pd.melt(df,id_vars='date',value_vars=df_col_name)
print(df_melt)


with sf.connect() as conn:
    try:
        conn.execute(f"USE SCHEMA PUBLIC")
        df_melt.insert(0,'FACTOR',factor_name)
        conn.execute('ALTER SESSION SET AUTOCOMMIT=TRUE')
        df_melt.to_sql(tbName, 
                            con=conn, 
                            chunksize=100000, 
                            index=False, 
                            schema= 'PUBLIC', 
                            method=pd_writer, 
                            if_exists="append",
                            dtype={
                                "FACTOR": sqlalchemy.types.VARCHAR(30),
                                "DATADATE": sqlalchemy.types.DateTime(),
                                "VARIABLE": sqlalchemy.types.VARCHAR(20),
                                "VALUE": sqlalchemy.types.FLOAT
                                }) 
    except Exception as e:
        print(e)
        myTeamsMessage.text(str(e))
        myTeamsMessage.send()
    finally:
        conn.close()
        # 다시 출력하게 하기
        # warnings.filterwarnings(action='default')

enddt= dt.datetime.now()

print(enddt)
# Comment send to Teams
fileName= sys.argv[0].split('/')
fileName=fileName[-1]  
file_comment= "fileName:\t\t**"+fileName+"**"
time_comment= "srt time:\t\t**"+str(srtdt)+"**\n\nend time:\t\t**"+str(enddt)+"**\n\nexecute time:\t\t**"+str(enddt- srtdt)+"**"
len_comment= "data_cnt:\t\t**"+str(len(df_melt))+"**"
#print(enddt)
sendcomment= file_comment+"\n\n"+time_comment+"\n\n"+len_comment

myTeamsMessage.text(sendcomment)
myTeamsMessage.send()