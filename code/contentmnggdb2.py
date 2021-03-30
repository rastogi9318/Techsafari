#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi,MySQLdb
f=cgi.FieldStorage();
id=f.getvalue("msg")
fln=f.getvalue("fln")
if fln==None:
	con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
	cur=con.cursor()
	cmd="delete from content where srn='"+str(id)+"'"
	cur.execute(cmd)
else:
	import os
	os.remove("../contentfile/"+fln+"")
	con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
	cur=con.cursor()
	cmd="delete from content where srn='"+str(id)+"'"
	cur.execute(cmd)
print'''
<script>
window.location.href='../bloger/contentmngg_blogger.py'
</script>
'''
