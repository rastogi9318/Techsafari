#!C:\Python27\python
print('Content-Type:text/html\n\n')
print("""
<html>
	<head>
		<link href="../images/icon.png" rel="icon"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<link href="../css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
		<link href="../css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
		<script src="../js/jquery.js"></script>
		<script src="../js/bootstrap.min.js"></script>
		<script src="../js/techSafari.js"></script>
		<script src="../js/techSafari1.js"></script>
		<link href="../css/index.css" rel="stylesheet" type="text/css"/>
		<link href="../css/loader.css" rel="stylesheet" type="text/css"/>
	</head>
<body> 
""")
exec(compile(source=open('blogger_header.py').read(),filename='blogger_header.py',mode='exec'));
print("""
<h1>Terms and condition:</h1>
<h4>This page is to define all the the terms and condition that you aggree by posting your blog on techSafari.com.</h4>

<p style="font-size:20px;">All the terms that you aggree are:<br/><br/>
1)That all the blog you post on this site are totally accurate as per your knowledge.<br/>
2)That if any user is having any kind of problem by using or reading or watching or listening your blog, the user can for sure go to court against you.The site or the owner or the developer will not responsible for the contents uploaded or the comment been made by the viewers.<br/>
3)The bloggers should put in their mind before uploading any video,audio,pdf or text type content on the site as if any action been taken against your blog then there will be no responsibility of the developer or the owner for your favour.<br/>
4)The owner will check the contents uploaded by the blogger, if they spot any suspicious material in your blog their account will be blocked and the content will be deleted from the site.<br/>
5)If your blogs are refering to any anti-national thought regarding to any country then your account will be blocked and it may happen the admin my take any strict action against you as this site is been sometime reached and used by the students and making any attempt of distracting them their goal is serious crime.</p>
</body>
</html>
""")