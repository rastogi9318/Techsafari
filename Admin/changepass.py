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
		<link href="../css/adminindex.css" type="text/css" rel="stylesheet"/>
		<link href="../css/login.css" type="text/css" rel="stylesheet"/>
	</head>
""")
exec(compile(source=open('adminheader.py').read(),filename='adminheader.py',mode='exec'))
print("""
<div class="col-sm-12  userlogin">
	<div class="col-sm-7 mainLogin">
		<div class="col-sm-12 fhead text-center"><span>Change Password</span></div>
		<form action="../code/changepassdb.py" method="post">
		<input type="password" name="opass", placeholder="Old Password"class="form-control" required/>
		<input name="npass" required="required" type="password" class="form-control" id="npass" placeholder="Password"/>
		<input name="cpass" required="required" class="form-control" type="password" id="cpass" oninput="check(this)" placeholder="confirm password"/>
			<input type="submit" class="form-control" id="btn" value="Change"/>
		</form>
	</div>
</div>
""")
exec(compile(source=open('adminfooter.py').read(),filename='adminfooter.py',mode='exec'))
print("""
</body>
</html>
""")