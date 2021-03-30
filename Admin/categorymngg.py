#!C:\Python27\python
print('Content-Type:text/html\n\n')
print("""
<html>
	<head>
		<link href="../images/icon.png" rel="icon"/>
		<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
		<link href="../css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<link href="../css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<script src="../js/jquery.js"></script>
		<script src="../js/bootstrap.min.js"></script>
		<link href="../css/adminindex.css" type="text/css" rel="stylesheet"/>
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
					<span>Category</span>
				</div>
			</div>
		<table class="table table-hover head2" border="1px">
			<tr style="background:black;color:white;">
				<th>Sr. No.</th>
				<th>Category</th>
				<th>Technology</th>
				<th>Delete</th>
			</tr>
""")
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="select srn,category,technology from category"
cur.execute(cmd)
res=cur.fetchall()
i=0
for a in res:
	i=i+1
	print"<tr><td>",i,"</td><td>",a[1],"</td><td>",a[2],"</td><td style='text-align:center;'><a href='../code/categorymnggdb.py?msg="+str(a[0])+"'style='text-decoration:none;font-size:25px;'><i class='fa fa-trash'style='color:orange;'></i></a></td></tr>"
print("""
		</table>
		</div>
	</div>
</div>
""")
exec(compile(source=open('adminfooter.py').read(),filename='adminfooter.py',mode='exec'))
print("""
</body>
</html>
""")