print("""
<div class="col-sm-12 main">
<div class="row">
	<div class="col-sm-12 mainHead">
						<div class="row">
							<div class="col-sm-12 head1">
								<div class="col-sm-4 tel">
									<a href="tel:7985464382"><i class="fa fa-phone" style="color:white;"></i> 7985464382</a>
								</div>
								<div class="col-sm-4 qot"><b>Tech Safari</b> Welcomes You!</div>
								<div class="col-sm-4 icon">
									<a target="blank"href="https://www.facebook.com"style="text-decoration:none;color:white;"><i class="fa fa-facebook"></i></a>
									<a target="blank"href="https://www.instagram.com"style="text-decoration:none;color:white;"><i class="fa fa-instagram"></i></a>
									<a target="blank"href="https://www.twitter.com"style="text-decoration:none;color:white;"><i class="fa fa-twitter"></i></a>
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
											<li><a href="index.py"><i class="fa fa-home"></i> Home</a></li>
											<li><a href="contactus.py">Contact Us</a></li>
											<li class="dropdown">
											 <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Tutorials <span class="caret"></span></a>
											  <ul class="dropdown-menu">
""")
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="select distinct technology from category where category='Tutorial' order by category asc"
cur.execute(cmd)
res=cur.fetchall()
for a in res:
 print"<li><a href='tutorial.py?type="+a[0]+"'>"+a[0]+"</a></li>"
print ("""

												
											  </ul>
											</li>
											<li class="dropdown">
											  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Examples<span class="caret"></span></a>
											  <ul class="dropdown-menu">
""")
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="select distinct technology from category where category='Examples' order by category asc"
cur.execute(cmd)
res=cur.fetchall()
for a in res:
 print"<li><a href='examples.py?type="+a[0]+"'>"+a[0]+"</a></li>"
print ("""
											  </ul>
											</li>
											<li class="dropdown">
											  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Exercises<span class="caret"></span></a>
											  <ul class="dropdown-menu">
""")
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","techSafari",3306)
cur=con.cursor()
cmd="select distinct technology from category where category='Exercises' order by category asc"
cur.execute(cmd)
res=cur.fetchall()
for a in res:
 print"<li><a href='exercises.py?type="+a[0]+"'>"+a[0]+"</a></li>"
print ("""
											  </ul>
											</li>
											<li><a target="blank" href="registration.py">Registation</a></li>
											<li class="dropdown">
											  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Login<span class="caret"></span></a>
											  <ul class="dropdown-menu">
												<li><a target="blank" href="login.py">Bloger Login</a></li>
												<li><a target="blank" href="adminLogin.py">Admin login</a></li>
											  </ul>
											</li>
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