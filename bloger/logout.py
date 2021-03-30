#!C:\Python27\python
print "Content-Type:text/html\n\n"
print("""
<html>
<head>
<script>
function logout()
{
window.history.forward;
window.setTimeout("window.location.href='../general/index.py'",1000);
}
</script>
</head>
<body onload="logout()">
</body>
</html>
""")