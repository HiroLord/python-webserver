import pymysql.cursors

def sqlGet(path):
	if (path == 'getName'):
		return getName();
	return "{}";

def getName():
	connection = pymysql.connect(host='192.168.1.110',
							user='Preston',
							passwd='password',
							db='dbTest',
							charset='utf8mb4',
							cursorclass=pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			sql = "SELECT name FROM Test"
			cursor.execute(sql, )
			result = cursor.fetchone()
			return result
	finally:
		connection.close();
