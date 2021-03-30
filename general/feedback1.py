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
exec(compile(source=open('header.py').read(),filename='header.py',mode='exec'));	
print("""
<div class="sol-sm-12 userlogin">
	<div class="col-sm-7 mainLogin">
	<div class="col-sm-12 fhead text-center"><span>Feedback</span>
	</div>
		<form action="../code/feedbackdb.py"method="post">
			<input type="email"name="email" required class="form-control" placeholder="Email"/>
	We need your valuable feedback!
			<textarea name="feedmsg"class="form-control" placeholder="feedback"style="height:100px;" class="feedback"></textarea>
			<input type="submit"class="form-control" id="btn" value="Feedback"/>
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