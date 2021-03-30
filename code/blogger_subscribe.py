#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
email=f.getvalue("email")
q="select email from subscribe"
cur.execute(q)
res=cur.fetchall()
i=0
for r in res:
	if r[0]==email:
		i+=1
		break;
	else:
		continue;
if i==0:
	cmd="insert into subscribe(email,date) values('"+str(email)+"',curdate())"
	cur.execute(cmd)
	print("<script>window.location.href='../bloger/blogger_index.py'</script>")
else:
	print("<script>window.location.href='../bloger/blogger_index.py';alert('already a  subscriber')</script>")
		