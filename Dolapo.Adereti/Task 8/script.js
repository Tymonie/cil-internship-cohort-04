let apiUrl = 'https://jsonplaceholder.typicode.com/users';
let listName = document.querySelector('.name');
let listMail = document.querySelector('.email');
let listUsername = document.querySelector('.username');
let listAddress = document.querySelector('.address');
let listPhoneno = document.querySelector('.phoneno');
let listWebsite = document.querySelector('.website');
let listCompanya = document.querySelector('.companyname');
let listCompanyb = document.querySelector('.companyinfo');

function displayList(response){
    let userName = response.data[0].name;
    let email = response.data[0].email; 
    let uName = response.data[0].username;
    let addy = response.data[0].address.street;
    let suite = response.data[0].address.suite;
    let city = response.data[0].address.city;
    let phone = response.data[0].phone;
    let web = response.data[0].website;
    let cname = response.data[0].company.name;
    let cinfo = response.data[0].company.catchPhrase;
    let cbs = response.data[0].company.bs;
    listName.innerHTML = `Name: ${userName}`;
    listUsername.innerHTML = `Username: ${uName}`;
    listMail.innerHTML = `E-mail: ${email}` ;
    listAddress.innerHTML = `Address: ${suite}, ${addy}, ${city}`;
    listPhoneno.innerHTML = `Phone no.: ${phone}` ;
    listWebsite.innerHTML = `Website: ${web}` ;
    listCompanya.innerHTML = `Company name: ${cname}` ;
    listCompanyb.innerHTML = `Company information: ${cinfo}, ${cbs}` ;

    console.log(apiUrl);
    console.log(response.data);
}

axios.get(apiUrl).then(displayList);