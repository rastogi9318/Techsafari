#!C:\Python27\python
print('Content-Type:text/html\n\n')
import cgi
import MySQLdb,os
import cgitb
import msvcrt
msvcrt.setmode(0,os.O_BINARY)
msvcrt.setmode(1,os.O_BINARY)
cgitb.enable()
f=cgi.FieldStorage()
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
blogger=f.getvalue("blogger")
category=f.getvalue("category")
technology=f.getvalue("technology")
ctopic=f.getvalue("content_topic")
ctype=f.getvalue("content_type")
if ctype=="Text": 
 cdescription=f.getvalue("desciption") 
 Q="insert into content(user,category,technology,ctopic,ctype,cdescription,curr_date) values('"+str(blogger)+"','"+str(category)+"','"+str(technology)+"','"+str(ctopic)+"','"+str(ctype)+"','"+str(cdescription)+"',curdate())"
else:
 media=f['media']
 fn=os.path.basename(media.filename)
 Q="insert into content(user,category,technology,ctopic,ctype,media,curr_date) values('"+str(blogger)+"','"+str(category)+"','"+str(technology)+"','"+str(ctopic)+"','"+str(ctype)+"','"+str(fn)+"',curdate())"
 open('../contentfile/'+fn,'wb').write(media.file.read())
cur.execute(Q)
print ("<script>window.location.href='../bloger/contentmngg_blogger.py'</script>")