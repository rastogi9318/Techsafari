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
		<link href="../css/hover-min.css" rel="stylesheet" type="text/css"/>
		<script src="../js/jquery.js"></script>
		<script src="../js/bootstrap.min.js"></script>
		<link href="../css/adminindex.css" rel="stylesheet" type="text/css"/>
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
					<span>Registrations done</span>
				</div>
			</div>
			<div class="col-sm-12">
			<div class="row">

""")
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="select name,email,mbn,dob,address,city,pincode,date from register"
cur.execute(cmd)
res=cur.fetchall()
i=0
for a in res:
	i=i+1
	print"""
	<div class="col-sm-6"style="border:1px solid black;">
	<h2>""",i,"""</h2>
	<h4><big>Name: </big>"""+str(a[0])+"""</h4>
	<h4><big>Email: </big>"""+str(a[1])+"""</h4>
	<h4><big>Mobile No.: </big>"""+str(a[2])+"""</h4>
	<h4><big>Date Of Birth: </big>"""+str(a[3])+"""</h4>
	<h4><big>Address: </big>"""+str(a[4])+""","""+str(a[5])+""","""+str(a[6])+"""</h4>
	<h4><big>Reg. Date: </big>"""+str(a[7])+"""</h4>
	<div class="text-right"><a href="../code/registermnggdb.py?msg="""+str(a[1])+""""style='text-decoration:none;'><i class='fa fa-trash'style='color:orange;font-size:20px;'></i></a></div></div>"""
print("""
		</div>
		</div>
		</div>
		</div>
	</div>
""")
exec(compile(source=open('adminfooter.py').read(),filename='adminfooter.py',mode='exec'))
