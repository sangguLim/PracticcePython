
import psycopg2 as pg
import pandas as pd

class Pgdb():
    def __init__(self,dbName:str=None):
        self.dbName=dbName
    def connPgdb(self):
        if  self.dbName==None or self.dbName=='a':
            conn = pg.connect(host='10.10.10.10', 
                        dbname='a_db',
                        user='postgres',
                        password='...',
                        port=50000)
        if self.dbName=='b':
            conn = pg.connect(host='10.10.10.10', 
                        dbname='b_db',
                        user='postgres',
                        password='...',
                        port=50000)
        if self.dbName=='c':
            conn = pg.connect(host='10.10.10.20', 
                        dbname='a_db',
                        user='postgres',
                        password='...',
                        port=5432)
        return conn