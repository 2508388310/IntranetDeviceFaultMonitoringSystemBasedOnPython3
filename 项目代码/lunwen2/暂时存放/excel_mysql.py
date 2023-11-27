import datetime
import pymysql
def time():
    start_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    global table_name
    table_name = 'time_{0}'.format(start_time)
def db_connect_config():
    db_connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='test',
        charset='utf8')
    # db_connection = database_connection()
    return db_connection
def db_connect(a):
    time()
    db_connection=db_connect_config()
    car = db_connection.cursor()
    try:
        sql_creat_table = 'create table {0}(' \
                          'id int(20)  AUTO_INCREMENT ,' \
                          '{1} char(100),' \
                          '{2} float,' \
                          '{3} char(10),' \
                          '{4} char(20),' \
                          '{5} char(100),' \
                          '{6} char(30),' \
                          'PRIMARY KEY (id));'\
            .format(table_name,a[0],a[1],a[2],a[3],a[4],a[5])
        print("1313232123")
        print(sql_creat_table)
        car.execute(sql_creat_table)  # 卸货
        db_connection.commit()

    except Exception as e:  # 方法一：捕获所有异常
        # 如果发生异常，则回滚
        print("发生异常:", e)
        db_connection.rollback()  # 执行rollbak；语句后又回到最初的数据状态
    finally:
        # 最终关闭数据库连接
        car.close()
        db_connection.close()
def insert_data(data):

    try:
        db_connection = db_connect_config()
        car = db_connection.cursor()

        sql_creat_table="insert into {0} values(null,'{1}','{2}','{3}'," \
                        "'{4}','{5}','{6}');".format(table_name,data[0],data[1],data[2],data[3],data[4],data[5])
        car.execute(sql_creat_table)  # 卸货
        db_connection.commit()
    except Exception as e:  # 方法一：捕获所有异常
        # 如果发生异常，则回滚
        print("发生异常:", e)
        db_connection.rollback()  # 执行rollbak；语句后又回到最初的数据状态
    finally:
        # 最终关闭数据库连接
        car.close()
        db_connection.close()
