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
		<link href="../css/index.css" rel="stylesheet" type="text/css"/>
		<link href="../css/login.css" rel="stylesheet" type="text/css"/>
</head>
<body>
""")
exec(compile(source=open('gheader.py').read(),filename='gheader.py',mode='exec'));	
print("""
<div class="sol-sm-12 userlogin">
	<div class="col-sm-7 mainLogin">
	<div class="col-sm-12 fhead text-center"><span>Login</span></div>
		<form action="../code/logindb.py"method="post">
			<input type="Email"name="email" required class="form-control" placeholder="Blogger's Email"/>
			<input type="password" name="pass"required class="form-control" placeholder="Blogging Password"/>
			<input type="submit"class="form-control" id="btn" value="Login"/>
		</form>
	</div>
</div>
""")
exec(compile(source=open('gfooter.py').read(),filename='gfooter.py',mode='exec'));
print("""
</div>
</body>
</html>
""")