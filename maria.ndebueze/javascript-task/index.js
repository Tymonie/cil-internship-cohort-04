var listOfUsers;

async function loadData() {
    
    await fetch('http://jsonplaceholder.typicode.com/users')
        .then((response) => response.json())
        .then((data) => {
            listOfUsers = data;
        });


    console.log(listOfUsers);

    for (const data in listOfUsers) {
        const user = listOfUsers[data];
        let tag = document.createElement("div");
        tag.innerHTML = `<div class="card">
         <div class="container">
           <h2><b>${user['name']}</b></h2>
           <p>username: ${user['username']}</p>
           <p>email: ${user['email']}</p>
           <p>street: ${user['address']['street']}</p>
           <p>suite: ${user['address']['suite']}</p>
           <p>city: ${user['address']['city']}</p>
           <p>zipcode: ${user['address']['zipcode']}</p>
           <p>lat: ${user['address']['geo']['lat']}</p>
           <p>lng: ${user['address']['geo']['lng']}</p>
           <p>phone: ${user['phone']}</p>
           <p>website: ${user['website']}</p>
           <p>name: ${user['company']['name']}</p>
           <p>catchPhrase: ${user['company']['catchPhrase']}</p>
           <p>bs: ${user['company']['bs']}</p>
         </div>
       </div>`;

       // document.createTextNode(JSON.stringify());
     
        var element = document.getElementById("body");
        element.appendChild(tag);
    }


}

loadData();