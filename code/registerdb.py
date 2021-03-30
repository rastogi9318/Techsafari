#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage()
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
name=f.getvalue('name')
email=f.getvalue('email')
mbn=f.getvalue('mbn')
dob=f.getvalue('dob')
city=f.getvalue('city')
address=f.getvalue('address')
pincode=f.getvalue('pincode')
password=f.getvalue('pass')
rq="insert into register values('"+str(name)+"','"+str(email)+"','"+str(mbn)+"','"+str(dob)+"','"+str(city)+"','"+str(address)+"','"+str(pincode)+"','"+str(password)+"',curdate())"
cur.execute(rq)
print("<script>window.location.href='../general/login.py'</script>")
