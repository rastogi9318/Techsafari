#!C:\Python27\python
print('Content-Type:text/html\n\n')
print(""" 
<html>
	<head>
		<link href="../images/icon.png" rel="icon"/>
		<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link href="../css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<link href="../css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
		<script src="../js/jquery.js"></script>
		<script src="../js/bootstrap.min.js"></script>
		<script src="../js/techSafari.js"></script>
		<script src="../js/techSafari1.js"></script>
		<link href="../css/index.css" rel="stylesheet" type="text/css"/>
	</head>
	<body>
""")
exec(compile(source=open('gheader.py').read(),filename='gheader.py',mode='exec'));	
print ("""
<div class="col-sm-12" style="background:#f9f9f9;min-height:500px">
<div class="row">
<button class="fa fa-bars" id="open"></button>
<div class="col-sm-2" id="sidemenu" style="background:white;box-shadow:0px 3px 2px #ffa500;min-height:100%;"><h3>
""")
import cgi,MySQLdb,os
import cgitb
import msvcrt
msvcrt.setmode(0,os.O_BINARY)
msvcrt.setmode(1,os.O_BINARY)
cgitb.enable()
f=cgi.FieldStorage();
type=f.getvalue("type")
print (""" 
"""+str(type)+""" Category<span id="close"><i class="fa fa-window-close" aria-hidden="true"></i></span>
</H3>
<hr/>
""")
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
q="select distinct ctopic from content where category='Examples' and Technology='"+type+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<a href='examplesbycategory.py?type="+type+"&topic="+r[0]+"'><h4><xmp>"+r[0]+"</xmp></h4></a>"
print ("""
</div>
<div class="ctype col-sm-2 text">Text</div>
<div class="col-sm-2 ctype video">Video</div>
<div class="col-sm-2 ctype audio">Audio</div>
<div class="col-sm-2 ctype pdf">Pdf</div>
<div class="col-sm-12 content">
<div class="col-sm-12" style="padding:5%;" id="text">
""")
q="select distinct ctopic from content where category='Examples' and ctype='text' and technology='"+type+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 q1="select * from content where category='Examples' and technology='"+type+"' and ctype='text'"
 cur.execute(q1)
 res1=cur.fetchall()
if res:
 for r1 in res1:
  print """<h2><xmp>""",r1[4],"""</xmp>
  </h2><hr/><pre style="font-size:20px;padding:1%;background:white;box-shadow:0px 1px 1px black"><code><xmp>"""+str(r1[6])+"""</xmp></code></pre> By : """,r1[1],""""""
else:
 print("<h1>Data Not Found!</h1>")
print ("""
</div>
<div class="col-sm-12" style="padding:5%;" id="video">
""")
q="select distinct ctopic from content where category='Examples' and ctype='Video' and technology='"+type+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 q1="select * from content where category='Examples' and technology='"+type+"' and ctype='Video'"
 cur.execute(q1)
 res1=cur.fetchall()
if res: 
 for r1 in res1:
  print """<h2><xmp>""",r1[4],"""</xmp>
  </h2><hr/><video controls width="100%"title="""+r[0]+"""><source src="../contentfile/"""+str(r1[7])+""""/></video><br/>By : """,r1[1],"""
  """
else:
 print("<h1>Data Not Found!</h1>")
print("""
</div>
<div class="col-sm-12" style="padding:5%;" id="audio">
""")
q="select distinct ctopic from content where category='Examples' and ctype='Audio' and technology='"+type+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 q1="select * from content where category='Examples' and technology='"+type+"' and ctype='Audio'"
 cur.execute(q1)
 res1=cur.fetchall()
if res:
 for r1 in res1:
  print """<h2><xmp>""",r1[4],"""</xmp>
  </h2><hr/><audio controls width="100%"><source src="../contentfile/"""+str(r1[7])+""""/></audio><br/>By : """,r1[1],"""
  """
else:
 print("<h1>Data Not Found!</h1>")
print("""
</div>
<div class="col-sm-12" style="padding:5%;" id="pdf">
""")
q="select distinct ctopic from content where category='Examples' and ctype='Pdf' and technology='"+type+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 q1="select * from content where category='Examples' and technology='"+type+"' and ctype='Pdf'and ctopic='"+r[0]+"'"
 cur.execute(q1)
 res1=cur.fetchall()
if res:
 for r1 in res1:
  print """<h2><xmp>""",r1[4],"""</xmp>
  </h2><hr/>
  <a href="../contentfile/"""+str(r1[7])+""""><i class="fa fa-file-pdf-o" aria-hidden="true"></i>""",r1[4],"""</a><br/>By : """,r1[1],"""
  """
else:
 print("<h1>Data Not Found!</h1>")
print("""
</div>
</div>
</div>
</div>
<!--Footer-->
""")
exec(compile(source=open('gfooter.py').read(),filename='gfooter.py',mode='exec'));
print("""
	</body>
</html>
""")