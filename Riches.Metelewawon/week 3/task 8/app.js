async function getUser() {
  const cardContainer = document.querySelector("#card-container");
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  const data = await res.json();
  data.forEach((user) => {
    cardContainer.innerHTML += `
         <div class="card">
           <ul> 
           <li>
           <div>
           <h1>Id:${user.id}</h1>
           <h5 id="fullName">Name: ${user.name}</h5>
           <h5 id="userName">Username: ${user.username}</h5>
           <h5 >Email: ${user.email}</h5>
           <h5>Address: ${user.address.street}, <br> Suite:${user.address.suite}, <br> City:${user.address.city}, <br> Zipcode:${user.address.zipcode}, <br> Geo: lat ${user.address.geo.lat}, lng:${user.address.geo.lng}</h5>
           <h5 >Phone: ${user.phone}</h5>
           <h5>Website: ${user.website}</h5>
           <h5>Company: ${user.company.name}</h5>
           <h5>Catchphrase: ${user.company.catchPhrase}</h5>
           <h5>bs: ${user.company.bs}</h5>
           
           </div>
           <li/>
           <ul/>
           
       </div>
 
      `;
  });
  console.log(data);
}
getUser();
