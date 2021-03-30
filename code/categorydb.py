#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
category=f.getvalue("category")
technology=f.getvalue("technology")
Q="insert into category (category,technology) values('"+str(category)+"','"+str(technology)+"')"
cur.execute(Q)
print("<script>window.location.href='../Admin/category.py'</script>")