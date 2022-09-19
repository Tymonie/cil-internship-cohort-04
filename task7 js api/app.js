const api = {
    base: "https://jsonplaceholder.typicode.com/users/"
}

const users = document.querySelector('#users');

function getResults () {
    fetch(`${api.base}`)
    .then(result => {
        return result.json();
    }).then(displayResults);
}

function displayResults (result) {
    console.log(result[0])
    let k = []
    for (i=0; i < 10; i++) {
        k.push(`{name : ${result[i].name}, email: ${result[i].email}, city: ${result[i].address.city}}\n`)
    }
    users.innerText = `${k}`
}

getResults()