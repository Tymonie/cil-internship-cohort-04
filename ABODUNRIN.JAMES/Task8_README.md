const loader = document.querySelector('.loader');
async function getUsers() {
  const url = 'https://jsonplaceholder.typicode.com/users';

  try {
    let response = await fetch(url);
    return await response.json();
  } catch (error) {
    console.log(error);
  }
}

async function renderUsers() {
  loader.style.display = 'block';
  let users = await getUsers();
  console.log(users);
  let html = '';
  users.forEach((user) => {
    let htmlSegment = `<div class="user">
                        <ul>
                            <li>${user.name}</li>
                            <li>${user.address.city}</li>
                            <li>${user.website}</li>
                            <li>${user.username}</li>
                            <li>${user.number}</li>
                            <li>${user.id}</li>
                        </ul>
                    </div>`;

    html += htmlSegment;
  });
  let usersContainer = document.querySelector('.usersContainer');
  usersContainer.innerHTML = html;
  loader.style.display = 'none';
}

renderUsers();

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title></title>
    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <nav class="nav"><h1>CIL Internship</h1></nav>
    <div class="container">
      <div class="loader"></div>
      <div class="usersContainer"></div>
    </div>
    <script src="index.js"></script>
  </body>
</html>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}



.nav {
    height: 10vh;
    background-color: grey;
    /* opacity: 0.2; */
    border-bottom: 1px solid black;

}

.nav h1 {
    text-align: center;
    color: black;
}


.loader {
    border: 16px solid #f3f3f3;
    /* Light grey */
    border-top: 16px solid #3498db;
    /* Blue */
    border-radius: 50%;
    position: absolute;
    left: 47%;
    top: 47%;
    width: 100px;
    height: 100px;
    animation: spin 2s linear infinite;

}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

.user {
    padding: 20px;
}
