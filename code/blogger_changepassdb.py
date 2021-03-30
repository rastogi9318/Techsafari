#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
email=f.getvalue("email")
opass=f.getvalue("opass")
cpass=f.getvalue("cpass")
Q="update register set password='"+str(cpass)+"' where email='"+str(email)+"' and password='"+str(opass)+"'";
cur.execute(Q)
res=cur.fetchall()
if res:
	print("""
	<script>
	window.location.href='../bloger/changepass_blogger.py'
	</script>
	""")
else:
	print("""
	<script>
	window.location.href='../general/login.py'
	</script>
	""")