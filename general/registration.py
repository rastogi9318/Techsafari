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
		<link href="../css/register.css" rel="stylesheet" type="text/css"/>
	</head>
	<body>
""")
exec(compile(source=open('gheader.py').read(),filename='gheader.py',mode='exec'));	
print("""
<div class="sol-sm-12 userlogin">
	<div class="col-sm-8 mainLogin">
	<div class="col-sm-12 fhead text-center"><span>Register</span></div>
		<form action="../code/registerdb.py" method="post">
		<div class="col-sm-6">
			Name <input type="text" required name="name"class="form-control" placeholder="Full Name"/>
			Email <input type="Email" required name="email" class="form-control" placeholder="Email"/>
			Mobile No.<input type="number" required name="mbn" placeholder="Mobile No." class="form-control"/>
			Date of Birth<input type="date" required name="dob" class="form-control"/>
		</div>
		<div class="col-sm-6">
			City<input type="text" required class="form-control"name="city" placeholder="City"/>
			Address<textarea placeholder="Address" class="form-control"name="address"></textarea>
			Pin Code<input type="number" maxLength="6"required class="form-control"name="pincode" placeholder="Pincode"/>
			Password<input name="pass" required="required" type="password" class="form-control" id="npass" placeholder="Password"/>
Confirm Password<input name="cpass" required="required" class="form-control" type="password" id="cpass" oninput="check(this)" placeholder="confirm password"/>
		</div>
			<input type="submit" id="btn"class="form-control text-center" value="Register"/>
		</form>
	</div>
</div>
""")
exec(compile(source=open('gfooter.py').read(),filename='gfooter.py',mode='exec'));
print("""
""")