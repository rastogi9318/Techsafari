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
		<link href="../css/index.css" type="text/css" rel="stylesheet"/>
		<link href="../css/login.css" type="text/css" rel="stylesheet"/>
	</head>
""")
exec(compile(source=open('blogger_header.py').read(),filename='blogger_header.py',mode='exec'))
print("""
<div class="col-sm-12 main">
	<div class="row">
		<div class="col-sm-12 head text-center">
			<div class="row">
				<div class="col-sm-12 head1"  style="color:white;margin:10px 0px;font-size:50px; background:black">
					<span>Contents added</span>
				</div>
			</div>
			<div class="col-sm-12">
			<div class="col-sm-3 ctype tut">Tutorial</div>
			<div class="col-sm-3 exp ctype" style="color:black;">Examples</div>
			<div class="col-sm-3 exc ctype" style="color:black;">Exercise</div>
			</div>
""")
import cgi,MySQLdb
f=cgi.FieldStorage();
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
q="select user,category,technology,ctopic,ctype,cdescription,media,curr_date,srn from content where user='"+ck+"' order by ctype"
cur.execute(q)
res=cur.fetchall()
print("""
		<div class="col-sm-12 text-left" id="tutorial" style="margin-bottom:20px;">
		<div class="row">
		<h1 class="text-center">Tutorial</h1>
""")
for r in res:
	if r[1]=='Tutorial':
		if r[4]=='Text':
			print("""
				<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3>
			<hr/><pre style="font-size:20px;padding:1%;background:white;box-shadow:0px 1px 1px black;line-height:15px;"><code><xmp>"""+str(r[5])+"""</xmp></code></pre><b>Date : """+str(r[7])+"""</b> <a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""" style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		elif r[4]=='Video':
			print("""
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/><video controls width="50%"title="""+r[3]+"""><source src="../contentfile/"""+str(r[6])+""""/></video><br/><br/>
			<b><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		elif r[4]=='Audio':
			print(""" 
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/><audio controls width="100%"><source src="../contentfile/"""+str(r[6])+""""/></audio><br/><br/>
			<b><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		else:
			print("""
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/>
			<a href="../contentfile/"""+str(r[6])+"""" target="black" id="inpdf"><i class="fa fa-file-pdf-o" aria-hidden="true"></i>"""+str(r[3])+"""</a>
			<br/><br/><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			<style>
			#inpdf{
			text-decoration:none;border:2px solid orange;color:black;padding:5px 10px;font-size:20px;
			}
			#inpdf:hover{
			border:2px solid black;
			color:orange;
			}
			#inpdf:hover i{
				color:red;
				font-weight:bold;
			}
			</style>
			
			""")
print("""	
		</div>
		</div>
		<div class="col-sm-12 text-left" id="examples" style="margin-bottom:20px;">
		<div class="row"><br/><br/>
		<h1 class="text-center">Examples</h1>
""")
for r in res:
	if r[1]=='Examples':
		if r[4]=='Text':
			print("""
				<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3>
			<hr/><pre style="font-size:20px;padding:1%;background:white;box-shadow:0px 1px 1px black;line-height:15px;"><code><xmp>"""+str(r[5])+"""</xmp></code></pre><b>Date : """+str(r[7])+"""</b> <a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""" style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		elif r[4]=='Video':
			print("""
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/><video controls width="50%"title="""+r[3]+"""><source src="../contentfile/"""+str(r[6])+""""/></video><br/><br/>
			<b><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		elif r[4]=='Audio':
			print(""" 
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/><audio controls width="100%"><source src="../contentfile/"""+str(r[6])+""""/></audio><br/><br/>
			<b><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		else:
			print("""
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/>
			<a href="../contentfile/"""+str(r[6])+"""" target="black" id="inpdf"><i class="fa fa-file-pdf-o" aria-hidden="true"></i>"""+str(r[3])+"""</a>
			<br/><br/><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			<style>
			#inpdf{
			text-decoration:none;border:2px solid orange;color:black;padding:5px 10px;font-size:20px;
			}
			#inpdf:hover{
			border:2px solid black;
			color:orange;
			}
			#inpdf:hover i{
				color:red;
				font-weight:bold;
			}
			</style>
			
			""")
print("""	
		</div>
		</div>
		<div class="col-sm-12 text-left" id="exercises" style="margin-bottom:20px;">
		<div class="row"><br/><br/>
		<h1 class="text-center">Exercises</h1>
""")
for r in res:
	if r[1]=='Exercises':
		if r[4]=='Text':
			print("""
				<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3>
			<hr/><pre style="font-size:20px;padding:1%;background:white;box-shadow:0px 1px 1px black;line-height:15px;"><code><xmp>"""+str(r[5])+"""</xmp></code></pre>
			<b>Date : """+str(r[7])+"""</b> <a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""" style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		elif r[4]=='Video':
			print("""
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/><video controls width="50%"title="""+r[3]+"""><source src="../contentfile/"""+str(r[6])+""""/></video><br/><br/>
			<b><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		elif r[4]=='Audio':
			print(""" 
			<div class="col-sm-12">
			<h3></xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/><audio controls width="100%"><source src="../contentfile/"""+str(r[6])+""""/></audio><br/><br/>
			<b><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			""")
		else:
			print("""
			<div class="col-sm-12">
			<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
			<hr/>
			<a href="../contentfile/"""+str(r[6])+"""" target="black" id="inpdf"><i class="fa fa-file-pdf-o" aria-hidden="true"></i>"""+str(r[3])+"""</a>
			<br/><br/><b>Date:"""+str(r[7])+"""</b><a href="../code/contentmnggdb2.py?msg="""+str(r[8])+"""&fln="""+str(r[6])+""""style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a>
			</div>
			<style>
			#inpdf{
			text-decoration:none;border:2px solid orange;color:black;padding:5px 10px;font-size:20px;
			}
			#inpdf:hover{
			border:2px solid black;
			color:orange;
			}
			#inpdf:hover i{
				color:red;
				font-weight:bold;
			}
			</style>
			
			""")
print("""	

		</div>
		</div>
		</div>
	</div>
</div>
""")
exec(compile(source=open('blogger_footer.py').read(),filename='blogger_footer.py',mode='exec'))
print("""
</body>
</html>
""")