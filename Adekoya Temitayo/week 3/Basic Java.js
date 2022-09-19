alert("sucess")

fetch('https://jsonplaceholder.typicode.com/users')
.then(Response => {
    return response.json();
})
.then(users => {
    console.log(users);
});
document.querySelector(".user")
