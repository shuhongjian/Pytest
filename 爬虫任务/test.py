import pymysql

# 链接数据库
conn = pymysql.connect(host="localhost", port=3306,user="root",passwd="123456",db="test")
# 创建游标对象
cursor = conn.cursor()

# 写sql，以及插入sql的参数
sql = "insert into taobao (`img_url`,`price`,`svolume`,`evaluate`,`integral`) values(%s,%s,%s,%s,%s)"
param=("2",10,'10',"1","1")
#param = pymysql.escape_string(param)

# 拼接完整sql,并执行
cursor.execute(sql,param)
# 提交
conn.commit()


# 关闭连接
conn.close()
cursor.close()