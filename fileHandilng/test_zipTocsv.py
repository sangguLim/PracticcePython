from typing import *
import json
import os
import zipfile
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL




# filenm = FPD_USMEDS
# date = 2022-10-24
# filenm = FPD_USMEDS_221024

class zipTocsv:
    def __init__(self, filenm: str,date: pd.Timestamp) -> None:
        self.filenm = filenm
        self.date_yymmdd = date.strftime('%y%m%d')
        self.txtfilefullnm = filenm+'.'+self.date_yymmdd
        self.csvfilefullnm = filenm+'_'+self.date_yymmdd
        self.date = date
        
    def replace_point(self):
        adjFilenm = self.txtfilefullnm.replace(".","_")
        return adjFilenm
    def _zip_file(self):
        PATH = 'D:\\Barra\\dailyZip\\'
        SAVE_PATH = 'D:\\Barra\\uncompress\\'

        with zipfile.ZipFile(PATH+ self.csvfilefullnm + '.zip', 'r') as existing_zip:
            existing_zip.extractall(SAVE_PATH)
    def _load_csv_file(self):  
        PATH= 'D:\\Barra\\uncompress\\'
        FOLD_PATH = self.filenm+'_'+self.date_yymmdd+'\\'
        SAVE_PATH = 'D:\\Barra\\daily\\'
        txtfile = pd.read_csv(PATH + FOLD_PATH + self.csvfilefullnm + ".csv")
        new_csv_file = txtfile.to_csv(SAVE_PATH + self.csvfilefullnm + ".csv")

    #def _load_csv_data(self,file_nm):




if __name__ == '__main__':
    a = zipTocsv('FPD_USMEDS','2022-10-24')
    a._zip_file(dt.datetime.now())
