#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
opass=f.getvalue("opass")
cpass=f.getvalue("cpass")
Q="update adminlogin set adminpass='"+str(cpass)+"' where adminpass='"+str(opass)+"'";
cur.execute(Q)
res=cur.fetchall()
if res:
	print("""
	<script>
	window.location.href='../Admin/changepass.py'
	</script>
	""")
else:
	print("""
	<script>
	window.location.href='../general/adminLogin.py'
	</script>
	""")