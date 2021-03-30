#!C:\Python27\python
print('Content-Type:text/html\n\n')
print(""" 
<html>
<head>
		<link href="../images/icon.png" rel="icon"/>
		<meta name="viewport" content="width=device-width,intial-scale=1.0"/>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link href="../css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<link href="../css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
		<script src="../js/jquery.js"></script>
		<script src="../js/bootstrap.min.js"></script>
		<script src="../js/techSafari.js"></script>
		<link href="../css/adminindex.css" rel="stylesheet" type="text/css"/>
	<style>
	.upperdash{
	min-height:100px;
	}
	.headdash{
	margin-top:4%
	color:black;
	font-family:Century Gothic;
	min-height:90px;
	line-height:90px;
	text-align:center;
	font-size:50px;
	}
	a .upd{
	text-decoration:none;
	color:black;
	min-height:250px;
	margin:2% 4%;
	text-align:center;
	font-weight:bold;
	font-size:20px;
	background:rgba(0,0,0,.1);
	}
	.lwd{
	text-decoration:none;
	color:black;
	min-height:250px;
	margin:2% 4%;
	text-align:center;
	font-weight:bold;
	font-size:20px;
	background:rgba(0,0,0,.1);
	}
	.upd .fa,.lwd .fa{
	font-size:140px;
	padding-top:15%;
	}
	</style>
</head>
<body>
""")
exec(compile(source=open('adminheader.py').read(),filename='adminheader.py',mode='exec'))
print("""
<div class="col-sm-12 headdash"><u>Admin's Dashboard</u></div>
<div class="col-sm-12 upperdash">
<div class="row">
	<div class="col-sm-1"></div>
	<div class="col-sm-10">
		<a href="category.py"><div class="col-sm-3 upd"><i class="fa fa-pencil-square-o" aria-hidden="true"></i><br/>Add Category</div></a>
		<a href="adminfeedbackmngg.py"><div class="col-sm-3 upd"><i class="fa fa-book" aria-hidden="true"></i><br/>Feedback</div></a>
		<a href="contentmngg.py"><div class="col-sm-3 upd"><i class="fa fa-tasks" aria-hidden="true"></i><br/>Content Management</div></a>
	</div>
	<div class="col-sm-1"></div>
</div>
</div>
<div class="col-sm-12 lowerdash">
<div class="row">
	<div class="col-sm-1"></div>
	<div class="col-sm-10">
		<div class="col-sm-2"></div>
		<a href="changepass.py"><div class="col-sm-3 lwd"><i class="fa fa-unlock-alt" aria-hidden="true"></i><br/>Change Password</div></a>
		<a href="logout.py"><div class="col-sm-3 lwd"><i class="fa fa-sign-out" aria-hidden="true"></i><br/>Logout</div></a>
		<div class="col-sm-2"></div>
	</div>
	<div class="col-sm-1"></div>
</div>
</div>
""")
exec(compile(source=open('adminfooter.py').read(),filename='adminfooter.py',mode='exec'))
print("""
</body>
</html>
""")