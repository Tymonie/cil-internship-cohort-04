const usermy = document.querySelector(".userm");

async function renderuser() {
  let listData = await fetch("https://jsonplaceholder.typicode.com/users");
  let list = await listData.json();
  console.log(list);
  list.forEach((details) => {
    let html = `<ul>
    <div class="det">
    <li><span>Name: </span> ${details.name}</li>
    <li><span>email: </span> ${details.email}</li>
    </div>
 
    </ul>`;
    usermy.insertAdjacentHTML("beforeend", html);
  });
}
renderuser();