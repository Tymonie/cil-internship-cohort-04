fetch('https://jsonplaceholder.typicode.com/users')
.then(function(response){
  return response.json();
})
.then(function(data){
  appendData(data)
})
.catch(function(err){
  console.log(err)
});

function appendData(data){
let container = document.getElementById('myData');
for(let i=0; i<data.length; i++){
let div = document.createElement('div');
div.innerHTML ='Name: ' + data[i].name  +  ' UserName: ' + data[i].username + ' Email: ' +  data[i].email +  'Id:' +  data[i].id +  'Street: ' +  data[i].address.street + ' Suite: ' +  data[i].address.suite + 'city: ' + data[i].address.city + 'zipcode: ' +  data[i].address.zipcode + ' lat: ' +  data[i].geo.lat + 'lng: ' + data[i].geo.lng;
container.appendChild(div);

}
}


