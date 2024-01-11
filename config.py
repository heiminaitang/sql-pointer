import pymysql
from pymysql.cursors import DictCursor

'''
配置信息
'''
pool_config = {
    'creator': pymysql,
    'user': '',
    'password': '',
    'host': '',
    'port': 3306,
    'database': '',
    'cursorclass': DictCursor,
    'mincached': 2, # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    'maxcached': 5, # 链接池中最多闲置的链接，0和None不限制
    'maxshared': 1, # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。

}