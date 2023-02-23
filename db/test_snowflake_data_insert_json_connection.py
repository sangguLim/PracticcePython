from typing import *
import json
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

from glue.snowflake import Snowflake


ACCOUNT_FP = "C:\\Users\\USER\\Documents\\alphaplatform-db\\etf_migration\\snowflake_update\\snowflake_account.json"

class DataInsert:
    def __init__(self, hldcode : int) -> None:
        #self.Table = Table
        self.hldcode = hldcode
        self.engine = self._get_engine()

    def _get_engine(self):
        with open(ACCOUNT_FP, "r") as f:
            account_info = json.load(f)

        return create_engine(URL(**account_info))
    def _load_test_tbl(self, date: pd.Timestamp):
        datestr = date.strftime("%Y-%m-%d")
        qry = f"select DATE,USA_HLD from alpha_platform.temp.date where usa_hld='{self.hldcode}' and date='{datestr}';"
        with self.engine.connect() as con:
            temp_date_data = pd.read_sql_query(qry, con)
            print(temp_date_data)
        return temp_date_data.set_index("date")
    def _read_to_scv(self):
        PATH = 'D:\\Barra\\daily\\'
        # 컬럼명 설정해서 불러오기
        data_result = pd.read_csv(PATH+'USA_XSEDOL_Asset_ID_20221216.csv'
                                    , sep=('|')
                                    ,header=1
                                    ,skiprows=0
                                    ,skipfooter=1
                                    , names = ['BarraId', 'AssetIDType', 'AssetID','StartDate','EndDate'])
        # barraID에 <index,ID>형태에서 ID만 남기게 전처리
        data_result = data_result.replace(r'[0-9]+\,','', regex=True)
    # def merge_dataframe_into_table(
    #     self,
    #     df: pd.DataFrame,
    #     table: Table,
    #     comp_cols: List[str],
    #     stage_prefix: str = "STAGE",
    # ):
    #     df = df[[col.name for col in table.columns]]
    #     stage_table = f"{stage_prefix}_{table.name}"

    #     with self.connect() as con:
    #         df.to_sql(stage_table, if_exists="fail", con=con, index=False)
    #         self.merge_into_table(stage_table, table, comp_cols=comp_cols)
    #     with self.connect() as con:
    #         con.execute(f"DROP TABLE {stage_table}")
    #def _load_csv_data(self,file_nm):




if __name__ == '__main__':
    a = DataInsert(1)
    a._load_test_tbl(dt.datetime.now())
