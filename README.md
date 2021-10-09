<!DOCTYPE html>

	<head> 
		<meta charset= "utf-8"/>
		<title>Home</title>
		<link rel="icon" href="https://www.publicdomainpictures.net/pictures/200000/velka/dragon-logo-symbol-silhouette.jpg">
		<link rel="stylesheet" type="text/css" href="website.css">
	</head>
	<!--website start-->
	<body>
		<!--nav bar-->
		<div class="container">
			<div class="nav-wrapper">
				<div class="left-side">
					<div class="nav-link-wrapper">
						<a href="home.html">Home</a>
					</div>

					<div class="nav-link-wrapper">
						<a href="about.html">About</a>
					</div>

					<div class="nav-link-wrapper">
							<a href="https://github.com/TheCheesyWiggle">Github</a>
					</div>

					<div class="nav-link-wrapper">
							<a href="mailto:fjlvanmontfort@gmail.com">Email</a>
					</div>
				</div>

				<div class="right-side">
					<div class="brand">
						<div>Finn van Montfort</div>
					</div>
				</div>
			</div>
			<!--showcase-->
			<div class ="content-wrapper">
				<div class="showcase-items-wrapper">
					<!--DOFE achievements-->
					<div class="showcase-item-wrapper">
						<div class="showcase-img-background" style = "background-image:url(images/portfolio1.jpg)"></div>	
						<div class="img-text-wrapper">
							<!--<div class="logo-wrapper">
								<img src="images/logos/quip.png" alt="">
							</div>-->

							<div class="subtitle">I have completed my DOFE silver and bronze awards.</div>
						</div>
					</div>
					<!--volunteering-->
					<div class="showcase-item-wrapper">
						<div class="showcase-img-background" style = "background-image:url(images/portfolio2.jpg)"></div>	
						<div class="img-text-wrapper">
							<!--<div class="logo-wrapper">
								<img src="images/logos/devcamp.png" alt="">
							</div>-->

							<div class="subtitle">I have coded my own game, a discord bot and this website. My primary language is java but i can also code python.</div>
						</div>
					</div>
					<!--Scouting achievements-->
					<div class="showcase-item-wrapper">
						<div class="showcase-img-background" style = "background-image:url(images/portfolio3.jpg)"></div>	
						<div class="img-text-wrapper">
							<!--<div class="logo-wrapper">
								<img src="images/logos/eventbrite.png" alt="">
							</div>-->

							<div class="subtitle">I have been involved in scouting for over 8 years allowing my to gain me chief scouts silver, gold and platinum.</div>
						</div>
					</div>
					<!--??-->
					<div class="showcase-item-wrapper">
						<div class="showcase-img-background" style = "background-image:url(images/portfolio4.jpg)"></div>	
						<div class="img-text-wrapper">
							<!--<div class="logo-wrapper">
								<img src="images/logos/shop-hacker.png" alt="">
							</div>-->

							<div class="subtitle">As far as work experience goes i have worked as barista/pizza chef at a local cafe for a month in the summer.</div>
						</div>
					</div>
					<!--coding achievements-->
					<div class="showcase-item-wrapper">
						<div class="showcase-img-background" style = "background-image:url(images/portfolio5.jpg)"></div>	
						<div class="img-text-wrapper">
							<!--<div class="logo-wrapper">
								<img src="images/logos/crondose.png" alt="">
							</div>-->

							<div class="subtitle">I volunteered as a young leader for a Beaver group for 3 years.</div>
						</div>
					</div>
					<!--dailysmarty-->
					<div class="showcase-item-wrapper">
						<div class="showcase-img-background" style = "background-image:url(images/portfolio6.jpg)"></div>	
						<div class="img-text-wrapper">
							<!--<div class="logo-wrapper">
								<img src="images/logos/dailysmarty.png" alt="">
							</div>-->

							<div class="subtitle">My future aim is to become a software engineer or to start a computer based company</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
	<script>
		const showcaseItems = document.querySelectorAll('.showcase-item-wrapper');

		showcaseItems.forEach(showcaseItem => {
    		showcaseItem.addEventListener('mouseover', () => {
    			console.log(showcaseItem.childNodes[1].classList);
    			showcaseItem.childNodes[1].classList.add('img-darken')
   			});
   			
   			showcaseItem.addEventListener('mouseout', () => {
      			console.log(showcaseItem.childNodes[1].classList)
      			showcaseItem.childNodes[1].classList.remove('img-darken');
    		});
  		});
	</script>
</html>
