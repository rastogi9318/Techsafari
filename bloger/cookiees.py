#!C:\Python27\python
import Cookie,cgi
cookie=Cookie.SimpleCookie()
cookie["user"]=cgi.FieldStorage().getvalue("email")
ck=cookie["user"]
print(ck)
print("Content-Type:text/html\n\n")
print("<script>window.location.href='blogger_index.py'</script>")