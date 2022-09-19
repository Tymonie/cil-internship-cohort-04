document.querySelector(".click").addEventListener('click', profile);
const url = "http://jsonplaceholder.typicode.com/users"

function profile() {
    fetch(url)
        .then(function (res) { return (res.json()) })
        .then(function (data) {
            let result = '<h1>Users Profile</h1>';
            data.forEach(function (user) {
                result += `
                            <ul>
                            <li> ID: ${user.id} </li>
                            <li> Name: ${user.name} </li>
                            <li> Email: ${user.email} </li>
                            <li> Address:${user.address.street}  ${user.address.suite} ${user.address.city}  </li>
                            <li> Phone: ${user.phone} </li>
                            <li> Usernamne: ${user.username} </li>
                            <li> Website: ${user.website} </li>
                            <li> Company Name: ${user.company.name} </li>
                             </ul>`
            }

            );
            document.querySelector(".output").innerHTML = result

        })
}
