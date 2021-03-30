#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
email=f.getvalue("adminemail")
password=f.getvalue("adminpass")
cmd="select * from adminlogin where adminemail='"+str(email)+"' and adminpass='"+str(password)+"'"
cur.execute(cmd)
res=cur.fetchall()
if res:
	print("""
	<script>
	window.location.href="../Admin/cookiees.py?email="""+str(email)+"""";
	</script>
	""")
else:
	print("""
	<script>
	window.location.href="../general/adminLogin.py";
	alert("Admin email or password is wrong!")
	</script>
	""")