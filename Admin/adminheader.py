import os,Cookie
try:
	cookie=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	ck=cookie["user"].value
	print("""
<body>
		<div class="col-sm-12 outer">
			<div class="row">
				<div class="col-sm-12 header">
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
											<li><a href="adminindex.py">Dashboard</a></li>
											<li><a href="changepass.py">Change Password</a></li>
											<li class="dropdown">
											  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Managment <span class="caret"></span></a>
											  <ul class="dropdown-menu">
												<li><a href="registrationmngg.py">Registration Managment</a></li>
												<li><a href="contentmngg.py">Content Managment</a></li>
												<li><a href="categorymngg.py">Category Managment</a></li>
												<li><a href="enquirymngg.py">Enquiry Managment</a></li>
												<li><a href="subscriber.py">Subscribers</a></li>
											</ul>
											</li>
											<li><a href="category.py">Add Category</a></li>
											<li><a href="adminfeedbackmngg.py">Feedback</a></li>
											<li><a href="logout.py">Logout</a></li>
											</li>
										  </ul>
										</div><!-- /.navbar-collapse -->
									  </div><!-- /.container-fluid -->
									</nav>
					</div>
				</div>
""")
except(Cookie.CookieError,KeyError):
	print("<script>window.location.href='../general/adminlogin.py'</script>")