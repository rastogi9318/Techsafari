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
		<script src="../js/techSafari1.js"></script>
		<script src="../js/techSafari.js"></script>
		<link href="../css/index.css" rel="stylesheet" type="text/css"/>
		<link href="../css/login.css" rel="stylesheet" type="text/css"/>
</head>
<body>
""")
exec(compile(source=open('blogger_header.py').read(),filename='blogger_header.py',mode='exec'))
print("""
<div class="sol-sm-12 userlogin">
	<div class="col-sm-7 mainLogin">
	<div class="col-sm-12 fhead text-center"><span>Add Content</span></div>
		<form action="../code/contentdb.py?blogger="""+ck+"""" method="post" enctype="multipart/form-data">
		<div class="col-sm-12">
		<div class="col-sm-6">
		<div class="row">
			Category<select name="category"required class="form-control">
			<option>Tutorial</option>
			<option>Examples</option>
			<option>Exercises</option>
			</select>
		</div>
		</div>
		<div class="col-sm-6">
		<div class="row">
			Technology<select class="form-control" name="technology">
""")
import cgi,MySQLdb
f=cgi.FieldStorage()
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="select distinct technology from category"
cur.execute(cmd)
res=cur.fetchall()
for r in res:
	print"<option>"+r[0]+"</option>"
print("""
			</select>
		</div>
		</div>
		<div class="col-sm-12">
		<div class="row">
			Content Topic<input type="text" required class="form-control" placeholder="Topic"name="content_topic"/>
			Content type<select required class="form-control" id="content_type" name="content_type">
			<option>--Content Type--</option>
			<option>Text</option>
			<option>Video</option>
			<option>Audio</option>
			<option>Pdf</option>
			</select>
			<div id="desciption">Content Description<textarea class="form-control"placeholder="Describe Here..."name="desciption"style="height:300px;"></textarea></div>
			<div id="media">Media blogs:<input type="file"class="form-control" name="media"style="background:transparent;border:none;box-shadow:none;"/></div>
		</div>
		</div>
			<input type="submit" class="form-control"id="btn" value="Add"/>
			<script>
</script>
		</form>
	</div>
</div>
""")
exec(compile(source=open('blogger_footer.py').read(),filename='blogger_footer.py',mode='exec'))
print("""
</body>
</html>
""")