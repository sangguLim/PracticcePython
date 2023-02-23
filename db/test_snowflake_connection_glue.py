from typing import Any, Callable, Dict, List, Optional
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.sql.schema import Column, Table
from glue.snowflake import Snowflake

class IdfMapper:
    def __init__(self,
            tblName = Optional[str] = None
        ):
        self.tblName = tblName
        self.keyValue = keyValue
        self.sf = Snowflake(
        role='alpha_platform',
        warehouse='COMPUTE_WH',
        user='sanggu.lim@qraftec.com',
        password='Dlatkdrn95!')
        #IDF_meta = pd.read_csv('./meta.csv')
        sf_conn = self.sf.connect()
    def get_seccode_value(self, dateValue):
        self.dateValue = dateValue
        if self.keyType == 1 : #GVKEY를 통한 SECCODE(QAID) 리턴
            temp = self.sf.read_sql(f"SELECT SECCODE FROM QA_VIEW.PUBLIC.VW_CSVSECURITYMAPPING WHERE GVKEY = {self.keyValue} AND '{dateValue}' BETWEEN STARTDATE  AND ENDDATE")
    def merge_dataframe_into_table(
        self,
        df: pd.DataFrame,
        table: Table,
        comp_cols: List[str],
        stage_prefix: str = "STAGE",
    ):
        df = df[[col.name for col in table.columns]]
        stage_table = f"{stage_prefix}_{table.name}"

        with self.connect() as con:
            df.to_sql(stage_table, if_exists="fail", con=con, index=False)
            self.merge_into_table(stage_table, table, comp_cols=comp_cols)
        with self.connect() as con:
            con.execute(f"DROP TABLE {stage_table}")
# 원본
# class IdfMapper:
#     def __init__(self,keyType,keyValue):
#         self.keyType = keyType
#         self.keyValue = keyValue
#         self.sf = Snowflake(
#         role='public',
#         warehouse='COMPUTE_WH',
#         user='jaehyeok.heo1@qraftec.com',
#         password='비밀입니다')
#         #IDF_meta = pd.read_csv('./meta.csv')
#         sf_conn = self.sf.connect()
#     def get_seccode_value(self, dateValue):
#         self.dateValue = dateValue
#         if self.keyType == 1 : #GVKEY를 통한 SECCODE(QAID) 리턴
#             temp = self.sf.read_sql(f"SELECT SECCODE FROM QA_VIEW.PUBLIC.VW_CSVSECURITYMAPPING WHERE GVKEY = {self.keyValue} AND '{dateValue}' BETWEEN STARTDATE  AND ENDDATE")



if __name__ == "__main__":
    IdfMapper('')