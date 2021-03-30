#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
email=f.getvalue('email')
messages=f.getvalue('msg')
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
Q="insert into contact (name,email,messages,dateon) values('"+str(name)+"','"+str(email)+"','"+str(messages)+"',curdate())"
cur.execute(Q);
print("""
<script>
window.location.href='../general/contactus.py';
</script>
""")