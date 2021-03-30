#!C:\Python27\python
import Cookie,cgi
cookie=Cookie.SimpleCookie()
cookie["user"]=cgi.FieldStorage().getvalue("email")
cookie["user"]
print(cookie["user"])
print("Content-Type:text/html\n\n")
print("<script>window.location.href='adminindex.py'</script>")