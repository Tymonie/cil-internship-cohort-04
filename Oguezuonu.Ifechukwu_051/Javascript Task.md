How to Use fetch () in JavaScript

When we talk about APIs, we also need to talk about endpoints. An endpoint is simply a unique URL you call to interact with another system.
Simply call fetch () with the endpoint URL as the argument:
Fetch ('https://ubahthebuilder.tech/posts/1');

The data returned from the API is not usually in a useable form. So you'll need to convert the data to a form which your JavaScript can operate with. Thankfully, you can use the json () method to do just that:
fetch('https://ubahthebuilder.tech/posts/1')
.then(data => {
return data.json();
})
.then(post => {
console.log(post.title);


