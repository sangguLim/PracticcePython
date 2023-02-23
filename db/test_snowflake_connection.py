import pandas as pd
from glue.snowflake import Snowflake

class IdfMapper:
    def __init__(self,keyType,keyValue):
        self.keyType = keyType
        self.keyValue = keyValue
        self.sf = Snowflake(
        role='public',
        warehouse='COMPUTE_WH',
        user='jaehyeok.heo1@qraftec.com',
        password='비밀입니다')
        #IDF_meta = pd.read_csv('./meta.csv')
        sf_conn = self.sf.connect()
    def get_seccode_value(self, dateValue):
        self.dateValue = dateValue
        if self.keyType == 1 : #GVKEY를 통한 SECCODE(QAID) 리턴
            temp = self.sf.read_sql(f"SELECT SECCODE FROM QA_VIEW.PUBLIC.VW_CSVSECURITYMAPPING WHERE GVKEY = {self.keyValue} AND '{dateValue}' BETWEEN STARTDATE  AND ENDDATE")