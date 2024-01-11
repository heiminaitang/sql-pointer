### 首先需要下载两个需要依赖的模块
```
pip install pymysql
pip install DBUtils
```
### 导入该模块和其配置
```
from sql_pioneer.source import Connection
from sql_pioneer.config import pool_config
```
### 配置数据库链接参数
```
pool_config['host'] = 'localhost'
pool_config['user'] = 'root'
pool_config['password'] = 'password'
pool_config['database'] = 'test'
```
### 创建连接池对象
```
connection = Connection(**pool_config)
```
### 执行sql语句
error用于接收sql语句执行过程中的异常信息  
result用于接收返回的结果，采用查询语句的时候返回正常的查询结果，修改语句的时候返回影响的记录数
```
error, result = connection.execute("select * from user")
```
