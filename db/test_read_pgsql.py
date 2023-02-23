import psycopg2 as pg
import pandas as pd


con = pg.connect(host='114.204.7.10', 
                    dbname='compustat_highlevel',
                    user='postgres',
                    password='qraft',
                    port=50000)

sql = '''select * from public.daily_famafrench_factor limit 10;'''
result = pd.read_sql(sql,con)
print(result)

#with pg.connect(con) as conn:


# cursor=db.cursor()
# cursor.execute(sql)

#print(result)

# def readDB(self,schema,table,colum):
#     sql = " SELECT {colum} from {schema}.{table}".format(colum=colum,schema=schema,table=table)
#     try:
#         self.cursor.execute(sql)
#         result = self.cursor.fetchall()
#     except Exception as e :
#         result = (" read DB err",e)
    
#     return result


# class Databases():
#     def __init__(self):
#         self.db = psycopg2.connect(host='localhost', dbname='test',user='postgres',password='password',port=5432)
#         self.cursor = self.db.cursor()

#     def __del__(self):
#         self.db.close()
#         self.cursor.close()

#     def execute(self,query,args={}):
#         self.cursor.execute(query,args)
#         row = self.cursor.fetchall()
#         return row

#     def commit(self):
#         self.cursor.commit()