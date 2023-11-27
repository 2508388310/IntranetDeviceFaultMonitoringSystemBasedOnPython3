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
                          '{1} char(20),' \
                          '{2} char(20),' \
                          '{3} char(20),' \
                          '{4} char(20),' \
                          '{5} char(20),' \
                          '{6} char(20),' \
                          '{7} char(20),' \
                          '{8} char(20),' \
                          '{9} char(20),' \
                          '{10} char(20),' \
                          '{11} char(20),' \
                          '{12} char(20),' \
                          '{13} char(20),'\
                          'PRIMARY KEY ( id ))'\
            .format(table_name,a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12])
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
    for i in data:
        a=i.split(';')
        print(a)
        try:
            db_connection = db_connect_config()
            car = db_connection.cursor()
            print(a[1])
            sql_creat_table="insert into {0} values(null,'{1}','{2}','{3}'," \
                            "'{4}','{5}','{6}'," \
                            "'{7}','{8}','{9}'," \
                            "'{10}','{11}','{12}'," \
                            "'{13}');".format(table_name,a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12])
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
