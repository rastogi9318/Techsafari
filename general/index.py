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
		<script src="../js/techSafari1.js"></script>
		<link href="../css/index.css" rel="stylesheet" type="text/css"/>
	</head>
	<body>
""")
exec(compile(source=open('gheader.py').read(),filename='gheader.py',mode='exec'));	
print ("""
							<div class="col-sm-12 head3">
								<div class="row">
								<div class="col-sm-1"></div>
								<div class="col-sm-10 sld">
								<div class="row">
									<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
									  <!-- Indicators -->
									  <ol class="carousel-indicators">
										<li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
										<li data-target="#carousel-example-generic" data-slide-to="1"></li>
									  </ol>
									  <!-- Wrapper for slides -->
									  <div class="carousel-inner" role="listbox">
										<div class="item active">
										  <img src="../images/1.jpg" alt="...">
										  <div class="carousel-caption cpt1">
										  Its <span><i>tech</i>Safari.....</span><br/>
										  </div>
										</div>
										<div class="item">
										  <img src="../images/7.jpg" alt="...">
										  <div class="carousel-caption cpt2">
											Time to share your idea with other on new technologies!
										  </div>
										</div>
									  </div>

									  <!-- Controls -->
									  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
										<span class="fa fa-chevron-left" aria-hidden="true"style="color:white;font-size:40px;margin-top:150%;"></></span>
										<span class="sr-only">Previous</span>
									  </a>
									  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
										<span class="fa fa-chevron-right" aria-hidden="true"style="color:white;font-size:40px;margin-top:150%;"></></span>
										<span class="sr-only">Next</span>
									  </a>
									</div>
									</div>
								</div>
								<div class="col-sm-1"></div>
								</div>
							</div>
						</div>
				</div>
				<div class="col-sm12 nmv">
					<div class="col-sm-1"></div>
					<div class="col-sm-10">
						<div class="col-sm-12">
							<div class="col-sm-6 N">
								<div class="col-sm-12" style="font-family:Century Gothic;color:black;font-size:70px;text-align:center;">
									N
								</div>
								<div class="col-sm-12">
									<p id="notify">Put your ideas and views on new technologies public!</p>
									<p id="notify2">Hey! wizards I am Yash Rastogi, I am the developer of this website and I welcome you to my website. I am a student of B.tech from "ABES ENGINEERING COLLEGE GHAZIABAD" in Computer Science & Engineering [CSE].
									<br/>	
										<br/>									
									!!THANK YOU FOR BEING HERE!!</p>
									<br/>
									<br/>
									
									<b onclick="notify()" id="readmoreN">Read more</b>
								</div>
							</div>
							<div class="col-sm-6 M">
								<div class="col-sm-12" style="font-family:Century Gothic;color:black;font-size:70px;text-align:center;">
									M/V
								</div>
								<div class="col-sm-12">
									<p id="ms">Put your ideas and views on new technologies public!</p>
									<p id="ms2">"Hey! This is the platform where you can share your knowledge on your specialized technology. There are many students and professional out there who need your knowledge and can grow with your help.<br/>As the good saying is that "Knowledge grows with sharing it with others". So please share your knowledge and also get knowledge from others as this is the biggest place for publicly sharing of the knowledge and also free for all.</p>
									<br/>
									<b onclick="mission1()" id="readmore">Read more</b>
								</div>
							</div>
							</div>
						</div>
					</div>
					<div class="col-sm-1"></div>
<div class="col-sm-12">
	<div class="row">
		<div class="col-sm-12 text-center indcontent"><h1><u>Contents Added</u></h1></div>
		<div class="col-sm-12">
""")
q="select user,category,technology,ctopic,ctype,cdescription,media,curr_date from content GROUP BY ctopic LIMIT 15";
cur.execute(q)
res=cur.fetchall()
for r in res:
	if r[4]=='Text':
		print("""
		<div class="col-sm-12"style="border-bottom:3px solid black;padding-bottom:4%;">
		<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
		<hr/><pre style="font-size:20px;padding:1%;background:white;box-shadow:0px 1px 1px black;line-height:15px;"><code><xmp>"""+str(r[5])+"""</xmp></code></pre> <b>By : """+str(r[0])+"""</b> on <b>Date : """+str(r[7])+"""</b>
		</div>
		""")
	elif r[4]=='Video':
		print("""
		<div class="col-sm-12"style="border-bottom:3px solid black;padding-bottom:4%;">
		<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
		<hr/><video controls width="80%"title="""+r[3]+"""><source src="../contentfile/"""+str(r[6])+""""/></video><br/>
		<b>By : """+str(r[0])+"""</b> on <b>Date:"""+str(r[7])+"""</b>
		</div>
		""")
	elif r[4]=='Audio':
		print(""" 
		<div class="col-sm-12"style="border-bottom:3px solid black;padding-bottom:4%;">
		<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
		<hr/><audio controls width="100%"><source src="../contentfile/"""+str(r[6])+""""/></audio><br/>
		<b>By : """+str(r[0])+"""</b> on <b>Date:"""+str(r[7])+"""</b>
		</div>
		""")
	else:
		print("""
		<div class="col-sm-12"style="border-bottom:3px solid black;padding-bottom:4%;">
		<h3><xmp>"""+str(r[2])+"""("""+str(r[3])+""")</xmp></h3><h4>"""+r[1]+"""</h4>
		<hr/>
		<a href="../contentfile/"""+str(r[6])+"""" target="black" id="inpdf"><i class="fa fa-file-pdf-o" aria-hidden="true"></i>"""+str(r[3])+"""</a>
		<br/><br/><b>By : """+str(r[0])+"""</b> on <b>Date:"""+str(r[7])+"""</b>
		</div>
		<style>
		#inpdf{
		text-decoration:none;border:2px solid orange;color:black;padding:5px 10px;font-size:20px;
		}
		#inpdf:hover{
		border:2px solid black;
		color:orange;
		}
		#inpdf:hover i{
			color:red;
			font-weight:bold;
		}
		</style>
		
		""")
print("""		
		</div>
	</div>
</div>
<!--Footer-->
""")
exec(compile(source=open('gfooter.py').read(),filename='gfooter.py',mode='exec'));
print("""
	</body>
</html>
""")