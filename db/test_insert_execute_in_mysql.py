import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, func
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, insert

temp_data = [{'time':'2019-02-07T14:01:00.000000000Z', 'temperature':68},
             {'time':'2019-02-07T14:02:00.000000000Z', 'temperature':69},
             {'time':'2019-02-07T14:03:00.000000000Z', 'temperature':70},
             {'time':'2019-02-07T14:04:00.000000000Z', 'temperature':71}]


date_string = '%Y-%m-%dT%H:%i:%S.%f000Z'
mysql_metadata = MetaData()
mysql_table = Table('temperature', mysql_metadata,
                    Column('time', DATETIME(fsp = 6), primary_key = True),
                    Column('temperature', INTEGER()))



def single_insert():
    engine = create_engine('mysql://test_user:test@localhost/temperature',
                                  echo = False)
    mysql_table.drop(engine, checkfirst = True)
    mysql_table.create(engine)
    conn = engine.connect()
    for row in temp_data:
        conn.execute(mysql_table.insert().values(time = func.STR_TO_DATE(row['time'], date_string),
                                                 temperature = row['temperature']))
def insert_many():
    engine = create_engine('mysql://test_user:test@localhost/temperature',
                                  echo = False)    
    mysql_table.drop(engine, checkfirst = True)
    mysql_table.create(engine)
    conn = engine.connect()
    conn.execute(mysql_table.insert(), temp_data)
    
def insert_many():
    engine = create_engine('mysql://test_user:test@localhost/temperature',
                                  echo = True)    
    mysql_table.drop(engine, checkfirst = True)
    mysql_table.create(engine)
    conn = engine.connect()
    stmt = text("INSERT INTO temperature VALUES( STR_TO_DATE(:time, '%Y-%m-%dT%H:%i:%S.%f000Z'), :temperature)")
    conn.execute(stmt, temp_data)

