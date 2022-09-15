<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script defer src="index.js"></script>
    <title>Javascript Task</title>

    <style>
        .det {
            width: 700px;
            display: flex;

        }

        li {
            margin: 20px;
            list-style: none;
        }

        li span {
            font-size: 20px;
            font-weight: 600;
        }
        .userlist {
            background-color: #ddd;
            padding: 1rem;
            margin-bottom: 1rem;
        }
    </style>
</head>

<body>

    <div class="userlist"></div>
</body>
<script>
    const usermy = document.querySelector(".userlist");

async function renderuser() {
  let listData = await fetch("https://jsonplaceholder.typicode.com/users");
  let list = await listData.json();
  console.log(list);
  list.forEach((details) => {
    let html = `<ul>
    <div class="det">
    <li><span>ID: </span> ${details.id}</li>
    <li><span>Name: </span> ${details.name}</li>
    <li><span>Username: </span> ${details.username}</li>
    <li><span>Email: </span> ${details.email}</li>
    </div>
 
    </ul>`;
    usermy.insertAdjacentHTML("beforeend", html);
  });
}
renderuser();
</script>
</html>
