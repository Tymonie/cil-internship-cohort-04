# Simple JS to call the backend API

```javascript

<html>
	<head>
		<title> user data </title>
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
		<script src="https://code.jquery.com/jquery-3.6.1.min.js"></script>
	</head>
	<body>
		<div class="container">
			<h2>Users</h2>
			<div id="users-list" class="row">
				<table class="table table-bordered table-striped">
					<thead>
						<th>Id</th>
						<th>Name</th>
						<th>Username</th>
						<th>Phone</th>
						<th>Email</th>
						<th>Website</th>
						<th>Address</th>
						<th>Company Info</th>
					</thead>
					<tbody id="users">
	
					</tbody>
				</table>
			</div>
		</div>
	
	<script>
		$( document ).ready(function() {
			loadData();
		});

		function loadData() {
			$.get("https://jsonplaceholder.typicode.com/users", (users) => {
				console.log(users);
				buildHtmlTableList(users);
				//buildHtmlCardList(users);
			});
		}

		function getUserAddress(address) {
			return address.suite + ", " + address.street
				+ ", " + address.city + ", " + address.zipcode +
				 " (Lat: " + address.geo.lat + ", Lng: " + address.geo.lng + ")";
		}

		function getUserCompany(company) {
			return "<strong>Name</strong>: " + company.name + "<br><br>" +
				"<strong>Catch Phrase</strong>: " + company.catchPhrase + "<br><br>" +
				"<strong>BS</strong>: " + company.bs;
		}

		function buildHtmlTableList(users) {
			console.log("building table list");
			let htmlString = "";
			for (user of users) {
				htmlString += "<tr>";
				htmlString += "<td>" + user.id + "</td>";
				htmlString += "<td>" + user.name + "</td>";
				htmlString += "<td>" + user.username + "</td>";
				htmlString += "<td>" + user.phone + "</td>";
				htmlString += "<td>" + user.email + "</td>";
				htmlString += "<td>" + user.website + "</td>";
				htmlString += "<td>" + getUserAddress(user.address) + "</td>";
				htmlString += "<td>" + getUserCompany(user.company) + "</td>";
				htmlString += "</tr>";
			}
			$("#users").html(htmlString);
		};

		function buildHtmlCardList(users) {
			console.log("building UL list");
			let htmlString = "";
			for (user of users) {
				htmlString += "<div class='card'>";
				htmlString += "<div class='card-header'>" + user.id + ".  " + user.name + "</div>";
				htmlString += "<div class='card-body'>";
				htmlString += "<strong>Username:</strong> " + user.username + "<br>";
				htmlString += "<strong>Phone:</strong> " + user.phone + "<br>";
				htmlString += "<strong>Email:</strong> " + user.email + "<br>";
				htmlString += "<strong>Website:</strong> " + user.website + "<br><br>";
				htmlString += "<strong>Address:</strong> " + getUserAddress(user.address) + "<br>";
				htmlString += "<h5 class='card-title'>Company Info</h5>" + getUserCompany(user.company);
				htmlString += "</div></div>";
			}
			$("#users-list").html(htmlString);
		};
	</script>
	</body>
</html>
```