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
		<link href="../css/adminindex.css" type="text/css" rel="stylesheet"/>
	</head>
	<body>
""")
exec(compile(source=open('adminheader.py').read(),filename='adminheader.py',mode='exec'))
print("""
<div class="col-sm-12 main">
	<div class="row">
		<div class="col-sm-12 head">
			<div class="row">
				<div class="col-sm-12 head1">
					<span>Enquiries submitted <i class="fa fa-user-circle"></i></span>
				</div>
			</div>
			<div class="col-sm-12">
			<div class="row">
""")
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="select eid,name,email,messages,dateon from contact"
cur.execute(cmd)
res=cur.fetchall()
i=0
for a in res:
	i=i+1
	print"""<div class='col-sm-6'style="border:1px solid #696969;">
	<h2>""",i,"""</h2>
	<h3><big>Name:</big>"""+str(a[1])+"""</h3>
	<h3><big>Email:</big>"""+str(a[2])+"""</h3>
	<h3>Message:</h3>
	<code style="font-size:22px;background:transparent;color:#696969;">"""+str(a[3])+"""</code>
	<h4><big>Date:</big>"""+str(a[4])+"""</h4>
	<div class="text-right">
	<a href='admincode/queryDel.py?msg="""+str(a[0])+"""'style='font-size:25px;text-decoration:none;'><i class='fa fa-trash'style='color:orange;'></i></a>
	</div>
	</div>"""
print("""
		</div>
		</div>
		</div>
	</div>
</div>
""")
exec(compile(source=open('adminfooter.py').read(),filename='adminfooter.py',mode='exec'))