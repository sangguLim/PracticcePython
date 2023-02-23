
import snowflake.connector
import pandas as pd
from glue.snowflake import Snowflake
import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,MetaData,Table, Column, Integer, String,TIMESTAMP,insert

myaccount='dob17693.us-east-1'
myrole='ALPHA_PLATFORM'
mywarehouse='COMPUTE_WH'
mydatabase='ALPHA_PLARFORM' 
myuser='sanggu.lim'
mypassword='Dlatkdrn95!'

# sf = Snowflake(
#     role='ALPHA_PLATFORM',
#     warehouse='COMPUTE_WH',   
#     database='ALPHA_PLARFORM' ,
#     user='sanggu.lim',
#     password='Dlatkdrn95!'    
# )
sf = Snowflake(
    role=myrole,
    warehouse=mywarehouse,   
    database=mydatabase ,
    user=myuser,
    password=mypassword
)

engine = create_engine(
            f"snowflake://{myuser}:{mypassword}@{myaccount}/{mydatabase}?role={myrole}&warehouse={mywarehouse}"
        )
sf_conn = sf.connect()
meta_data = MetaData(bind=engine)

qry = '''use schema temp;'''
sf.read_sql(qry)

"""
insert_table= Table(
    'TEST_TABLE',   # db 내 저장될 table name
    meta_data,
    Column('data_date',TIMESTAMP,primary_key=True), # 이 테이블에 들어갈 컬럼입니다
    Column('usl_hld',Integer)
)

stmt = insert(insert_table).values(data_date='2022-12-26', usl_hld=1)
print(stmt)
compiled = stmt.compile()
print(compiled.params)

with engine.connect() as sf_conn:
    result= sf_conn.execute(stmt)
    sf_conn.commit()

# insert 대상 리스트
insert_list= [('2022-12-26', 1),('2022-12-27', 2)]
insert_df= pd.DataFrame(insert_list,columns=['DATA_DATE','USL_HLD'])
print(insert_df)

# 컬럼명
comp_col= ['DATA_DATE','USL_HLD']

print(comp_col)
print(type(comp_col))
#insertExec = sc.cursor().executemany("insert into alpha_platform.temp.test_table(DATA_DATE,USL_HLD) VALUES(?,?)",insert_list)
sf.merge_dataframe_into_table(insert_df,insert_table,insert_table.c.keys())
#cur = sf.cursor()
#cur.execute("select * from alpha_platform.temp.test_table;")

"""
sf_conn.close()
