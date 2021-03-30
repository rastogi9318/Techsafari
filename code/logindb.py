#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage()
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
email=f.getvalue("email")
password=f.getvalue("pass")
cmd="select * from register where email='"+str(email)+"' and password='"+str(password)+"'"
cur.execute(cmd)
res=cur.fetchall()
if res:
	print("<script>window.location.href='../bloger/cookiees.py?email="+str(email)+"'</script>")
else:
	print("<script>alert('Wrong Email or Password');window.location.href='../general/login.py';</script>")