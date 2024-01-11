import traceback

from dbutils.pooled_db import PooledDB


class Connection:
    def __init__(self, **pool_config):
        self.pool = PooledDB(**pool_config)
        print("数据库连接池创建成功......")

    '''
    执行sql语句
    '''
    def execute(self, sql, args=()):
        error, result = None, None
        connection = self.pool.connection()  # 创建链接对象
        cursor = connection.cursor()  # 创建游标对象
        try:
            cursor.execute(sql, args)  # 执行sql语句
            if not sql.split()[0].lower() != "select":
                connection.commit()  # 提交事务
                result = cursor.rowcount
            else:
                result = cursor.fetchall()  # 获取结果
        except Exception as err:
            connection.rollback()  # 回滚事务
            error = traceback.format_exc()
            result = False
        finally:
            cursor.close()  # 关闭游标对象
            connection.close()  # 关闭链接对象
        return error, result

    '''
    析构方法
    '''
    def __del__(self):
        self.pool.close()  # 关闭连接池
        print("数据库连接池资源已释放.......")