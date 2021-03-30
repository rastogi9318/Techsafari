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
		<link href="../css/contactus.css" rel="stylesheet" type="text/css"/>
	</head>
	<body>
""")
exec(compile(source=open('gheader.py').read(),filename='gheader.py',mode='exec'));		
print("""
							<div class="col-sm-12 mydetails">
								<div class="col-sm-3 location">
								<h2><i class="fa fa-map-marker"></i> Location</h3>
								<p>Fatehpur<br/>
								Mahadevan Tola <br/>
								Fatehpur(U.P),212601</p> 
								</div>
								<div class="col-sm-3 location">
									<h2><i class="fa fa-phone"></i> Contacts</h2><br/>
									<p>Personal: 7985464382<br/>
									<br/>Office: 7376890952<br/>
									
								</div>
								<div class="col-sm-3 location">
								<h2><i class="fa fa-envelope"></i>Emails</h2><br/>
								<p>yash20000rastogi@gmail.com<br/><br/>
								yash.20b0103003@abes.ac.in<br/></p>
								
								</div>
								<div class="col-sm-12 query">
									<div class="col-sm-12 qform">
										<div class="col-sm-2"></div><!--waist-->
										<div class="col-sm-8 qmainform">
									<div class="col-sm-12" id="Queryy">Query!</div>
											<form action="../code/Query.py" method="post">
												<input type="text" class="form-control" name="name" placeholder="Name"/>
												<input type="email" class="form-control" name="email" placeholder="Email"/>
												<textarea class="form-control" name="msg" placeholder="Query..."style="height:100px;"></textarea>
												<input type="submit" value="Send Query"/>
											</form>
										</div>
										<div class="col-sm-2"></div><!--waist-->
									</div>
									
								</div>
							</div>
							<div class="col-sm-12 gmap">
							
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6024.790941544655!2d80.81741584049047!3d25.929902290573782!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399b62ac2e0544c9%3A0xc42a3ca1a1a49ac!2sBaqar%20Ganj%2C%20Vaqeer%20Ganj%2C%20Fatehpur%2C%20Uttar%20Pradesh%20212601!5e0!3m2!1sen!2sin!4v1609354718981!5m2!1sen!2sin" width="100%" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>						</div>

							</div>
							<!--Footer-->
""")
exec(compile(source=open('gfooter.py').read(),filename='gfooter.py',mode='exec'));
print("""
	</body>
</html>
""")