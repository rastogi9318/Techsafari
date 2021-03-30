#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
id=f.getvalue("msg")
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="delete from feedback where srn='"+str(id)+"'";
cur.execute(cmd)
print'''
<script>
window.location.href='../Admin/adminfeedbackmngg.py'
</script>
'''
