from alphaju import get_factor_data
import pandas as pd
import sys
import sqlalchemy
import datetime as dt

sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon
import connTeams

class TeamsLog:
    def __init__(self,WebHook: str = None):
        self.WebHook= connTeams.webhook(WebHook)
        self.TeamsMsg = connTeams.pymsteams.connectorcard(self.WebHook)      
    def sendMsg(self, 
                fileName:str,
                srtTime: dt.datetime,
                df: pd.DataFrame = None,
                objName: str = None
                ):
        """
        # file명 추출 코드
        fileName= sys.argv[0].split('/')
        fileName=fileName[-1]  
        """
        # comment 설정
        file_comment= "> fileName:\t\t**"+fileName+"**<br/>"
        endTime= dt.datetime.now()        
        time_comment= "srt time:\t\t**"+str(srtTime)+"**<br/>end time:\t\t**"+str(endTime)+"**<br/>execute time:\t\t**"+str(endTime- srtTime)+"**<br/>"
        if not df==None:
            len_comment= "data_cnt:\t\t**"+str(len(df))+"**<br/>"
        else:
            len_comment=""
        
        if not objName==None:
            factor_comment= "factorName:\t\t**"+objName+"**<br/>"
        else:
            factor_comment=""

        send_comment= file_comment+factor_comment+time_comment+len_comment

        self.TeamsMsg.text(send_comment)
        self.TeamsMsg.send()

fileName= sys.argv[0].split('/')
fileName=fileName[-1]  
srtTime= dt.datetime.now()

TeamsSend= TeamsLog('FactorReport')
TeamsSend.sendMsg(fileName,srtTime)