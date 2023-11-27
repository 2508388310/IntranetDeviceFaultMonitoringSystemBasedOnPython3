import threading
import cryptography

import pymysql
import time
import datetime
import socket
import test
import _thread
hostname = socket.gethostname()
locallhost = socket.gethostbyname(hostname)#本地ip
def time():
    start_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    global table_name
    table_name = 'time_{0}'.format(start_time)

    # return table_name

# def database_connection():
#     global db_connection
def db_template(sql_statement):
    db_connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='test',
        charset='utf8')
    # db_connection = database_connection()
    car = db_connection.cursor()  # pymysql.connect是高速公路，conn.cursor()是运送的小车
    try:
        sql_statement = sql_statement
        car.execute(sql_statement)  # 卸货
        db_connection.commit()
          # mysql返回值
        #print(car.fetchone())
    except Exception as e:  # 方法一：捕获所有异常
        # 如果发生异常，则回滚
        print("发生异常:", e)
        db_connection.rollback()#执行rollbak；语句后又回到最初的数据状态
    finally:
        # 最终关闭数据库连接
        car.close()
        db_connection.close()

def creat_table():
    print("aaaaaaaaa")
    # db_connection=database_connection()
    # creat_table_car = db_connection.cursor()  # pymysql.connect是高速公路，conn.cursor()是运送的小车
    time()
    sql_creat_table = 'create table {0}(id int(11)  AUTO_INCREMENT ,源IP char(20) DEFAULT NULL,' \
                      '目标IP char(20) DEFAULT NULL,通讯状态 char(100) DEFAULT NULL ,symbol int(2) default null ,' \
                      '线程运行名 char(20) DEFAULT NULL,时间 char(40),PRIMARY KEY ( id ))'.format(table_name)
    db_template(sql_creat_table)


def insert_new_data(target_ip, icmp_result,symbol=0,name='null'):#,locallhost,target_ip,icmp_result#需要这些数据
    ceshitime = datetime.datetime.now().strftime('%H%M%S')
    # table_name1=table_name
    locallhost1=locallhost
    target_ip1=target_ip
    icmp_result1=icmp_result
    sql_insert_data="insert into {0} values(null,'{1}','{2}','{3}','{4}','{5}','{6}');".format(table_name,locallhost1,target_ip1,icmp_result1,symbol,name,ceshitime)
    db_template(sql_insert_data)
    # insert_new_data_car.execute(sql_insert_data)
    # db_connection.commit()
    # insert_new_data_car.fetchone()
    # insert_new_data_car.close()
    # db_connection.close()