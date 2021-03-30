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
		<link href="../css/adminindex.css" rel="stylesheet" type="text/css"/>
		<link href="../css/login.css" rel="stylesheet" type="text/css"/>
		
</head>
<body>
""")
exec(compile(source=open('adminheader.py').read(),filename='adminheader.py',mode='exec'))
print("""
<div class="sol-sm-12 userlogin">
	<div class="col-sm-7 mainLogin">
	<div class="col-sm-12 fhead text-center"><span>Add Category</span></div>
		<form action="../code/categorydb.py" method="post">
			Category<select name="category"class="form-control">
			<option>Tutorial</option>
			<option>Examples</option>
			<option>Exercises</option>
			</select>
			Technology
			<input type="text" name="technology"required class="form-control" />
			<input type="submit"class="form-control" id="btn" value="Add now"/>
		</form>
	</div>
</div>
""")
exec(compile(source=open('adminfooter.py').read(),filename='adminfooter.py',mode='exec'))
print("""
</body>
</html>
""")