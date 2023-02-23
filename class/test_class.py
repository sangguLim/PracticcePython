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

class FactorInsDB:
    def __init__(self,factorName: str):
        self.factorName= factorName
        self.srtTime= dt.datetime.now()
    def melting(self,freq: str):
        df= get_factor_data(self.factorName,freq=freq)
        df_col_name = df.columns
        df=df.reset_index()
        self.df_melt = pd.melt(df,id_vars='date',value_vars=df_col_name)
        return self.df_melt
    def TeamsLog(self):  
        WebHook= connTeams.webhook()
        myTeamsMessage = connTeams.pymsteams.connectorcard(WebHook)      
        self.endTime= dt.datetime.now()
        fileName= sys.argv[0].split('/')
        fileName=fileName[-1]  
        file_comment= "fileName:\t\t**"+fileName+"**"
        time_comment= "srt time:\t\t**"+str(srtdt)+"**\n\nend time:\t\t**"+str(self.endTime)+"**\n\nexecute time:\t\t**"+str(self.endTime- self.srtTime)+"**"
        len_comment= "data_cnt:\t\t**"+str(len(self.df_melt))+"**"
        #print(enddt)
        sendcomment= file_comment+"\n\n"+time_comment+"\n\n"+len_comment

        myTeamsMessage.text(sendcomment)
        myTeamsMessage.send()
    def ins_sf(self):
        sf= sfcon.sf()
        tbName= 'FACTOR_LONGFORM'

        with sf.connect() as conn:
            try:
                conn.execute(f"USE SCHEMA PUBLIC")
                df_melt= self.melting("A")
                df_melt.insert(0,'FACTOR',self.factorName)
                conn.execute('ALTER SESSION SET AUTOCOMMIT=TRUE')
                df_melt.to_sql(tbName,
                                con= conn,
                                chunksize= 100000,
                                index=False,
                                schema='PUBLIC',
                                method= pd_writer,
                                if_exists="append",
                                dtype={
                                    'FACTOR': sqlalchemy.types.VARCHAR(30),
                                    'DATE': sqlalchemy.types.DateTime(),
                                    'VARIABLE': sqlalchemy.types.VARCHAR(20),
                                    'VALUE': sqlalchemy.types.FLOAT
                                })
            except Exception as e:
                print(e)
            finally:
                conn.close()
                self.TeamsLog()
