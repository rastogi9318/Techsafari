#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
email=f.getvalue("email")
msg=f.getvalue("feedmsg")
cmd="insert into feedback(email,msg,date) values('"+str(email)+"','"+str(msg)+"',curdate())"
cur.execute(cmd)
print("<script>window.location.href='../general/index.py'</script>")