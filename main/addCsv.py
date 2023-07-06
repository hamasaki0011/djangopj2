from django.db import connection
import logging
import csv
from datetime import datetime as dt

logger=logging.getLogger('development')

# SQL for adding the data
sql_insert=(("insert into result (measured_date, measured_value, point_id, place_id, created_date, updated_date) "
              "select * from (select cast(%s as timestamp) as measured_date, cast(%s as numeric) as measured_value, cast(%sas numeric) as point_id, cast(%s as numeric) as place_id, "
              "cast(%s as timestamp) as created_date, cast(%s as timestamp) as updated_date) as tmp "
              "where not exists (select * from result where point_id = cast(%s as numeric) and measured_date = cast(%s as timestamp))"))

# (
#     "insert into result (measured_date, measured_value, point_id, place_id, created_date, updated_date) "
#     "select * from (%s as measured_date, %s as measured_value, %s as point_id, %s as place_id, %s as created_date, %s as updated_date) as tmp "
#     "where not exists (select * from result where point_id = %s and measured_date = %s)"
# )

def read_data(cursor,file_path):
    # read csv file
    try:
        file=open(file_path,newline='')
    except IOError:
        logger.warning('対象ファイルがありません:'+file_path)
        logger.warning('DB登録は行いません:'+file_path)
    else:
        logger.info('=== > Start D B登録 ===')
        with file:
            #2023.7.6 Change read method into Dictionary-base
            reader=csv.reader(file)
            header=next(reader) # dummy sentence to skip header line
            #23.7.6 reader=csv.DictReader(file)

            """ tuple format of add_data
            [0,             ,1              ,2          ,3]  
            [measure_date, measured_value, point_id, place_id
            point_id is referenced to sensors.id
            """
            for row in reader:
                str_time=[dt.now().strftime('%Y-%m-%d %H:%M:%S')]
                add_data=[]
                """ .append(): 末尾に要素を追加
                    .extend(): 末尾に連結する、別のリストやタプル
                    .insert(): 指定位置に要素を挿入する
                """
                # extend array "add_data" and add the read data from csv file
                add_data.extend(row)        
                add_data.extend(str_time)   # add created_date area
                add_data.extend(str_time)   # add updated_date area
                add_data.append(row[2])     # point_id(対象レコードがDBに存在するかの確認用)
                add_data.append(row[0])     # 対象日時(対象レコードがDBに存在するかの確認用)

                # add_data.append(row.get('measured_date'))
                # add_data.append(row.get('measured_value'))
                # add_data.append(row.get('point_id'))
                # add_data.append(row.get('place_id'))
                # add_data.extend(str_time)       # created_date
                # add_data.extend(str_time)       # updated_date

                # add_data.append(row.get('point_id'))
                # add_data.append(row.get('measured_date'))

                logger.debug('add_data='+str(add_data))

                # add the record
                cursor.execute(sql_insert,add_data)

            logger.info("=== End DB登録 < ===")

# Register the data in csv file to DataBase
def insert_csv_data(file_path):
    logger.info('=== csvデータ登録開始 ===')

    with connection.cursor() as cursor:
        read_data(cursor,file_path)

    logger.info('=== csvデータ登録処理終了 ===')