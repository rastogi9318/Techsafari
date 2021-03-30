print("""
<div class="col-sm-12 main">
<div class="row">
	<div class="col-sm-12 mainHead">
		<div class="row">
			<div class="col-sm-12 head1">
				<div class="col-sm-4 tel">
					<a href="tel:7985464382">
""")
import os,Cookie
try:
	cookie=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	ck=cookie["user"].value
	print(ck)
except(Cookie.CookieError,KeyError):
	print("<script>window.location.href='../general/index.py'</script>")
print("""
</a>
								</div>
								<div class="col-sm-4 qot"><b>Tech Safari</b> Welcomes You!</div>
								<div class="col-sm-4 icon">
									<i class="fa fa-facebook"></i>
									<i class="fa fa-instagram"></i>
									<i class="fa fa-twitter"></i>
								</div>
							</div>
							<div class="col-sm-12 head2">
								<div class="col-sm-2 logo">
								<span><i>tech</i>Safari</span>
								</div>
								<div class="col-sm-10 menu">
									<nav class="navbar navbar-default" id="menu">
										<div class="container-fluid">
										<!-- Brand and toggle get grouped for better mobile display -->
										<div class="navbar-header">
										  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
											<span class="sr-only clpbtn">Toggle navigation</span>
											<span class="icon-bar"></span>
											<span class="icon-bar"></span>
											<span class="icon-bar"></span>
										  </button>
										</div>

										<!-- Collect the nav links, forms, and other content for toggling -->
										<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1" >
										  <ul class="nav navbar-nav navbar-right">
											<li><a href="blogger_index.py"><i class="fa fa-dashboard"></i> Dashboard</a></li>
											<li><a href="content.py">Add Content</a></li>
											<li><a href="contentmngg_blogger.py">Content Management</a></li>
											<li><a href="changepass_blogger.py">Change Password</a></li>
											<li><a href="logout.py">Logout</a></li>
										  </ul>
										</div><!-- /.navbar-collapse -->
									  </div><!-- /.container-fluid -->
									</nav>
								</div>
							</div>
</div>
</div>
</div>
</div>
""")