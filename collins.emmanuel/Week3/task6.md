// Original file name is 'users.js' and 'users.html'

async function getUsers() {
    let url = 'https://jsonplaceholder.typicode.com/users';
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function renderUsers() {
    let users = await getUsers();
    let html = '';
    users.forEach(user => {
        let htmlSegment = `<div class="user">
                            <h2>User (${user.id})</h2>
                            <p><b>Name</b>: ${user.name},</p>
                            <p><b>Username</b>: ${user.username},</p>
                            <h4>Address-</h4>
                            <p><b>Street</b>: </p>${user.address.street},</p>
                            <p><b>Suite</b>: ${user.address.suite},</p>
                            <p><b>City</b>: ${user.address.city},</p>
                            <p><b>Zip code</b>: ${user.address.zipcode},</p>
                            <p><b>Latitude</b>: ${user.address.geo.lat},</p>
                            <p><b>Longitude</b>: ${user.address.lng},</p>
                            <div class="email">send me a mail via<a href="email:${user.email}"> ${user.email}</a>,</div>
                            <p><b>Phone number</b>: ${user.phone},</p>
                            <p><b>Website</b>:<a href="${user.website}"> ${user.website}</a>,</p>
                            <h4>Company-</h4>
                           <p><b>Name</b>: ${user.company.name},</p>
                           <p><b>Catch phrase</b>: ${user.company.catchPhrase},</p>
                           <p><b>BS</b>: ${user.company.bs}.</p>
                        </div>
                           <hr>`;

        html += htmlSegment;
    });

    let container = document.querySelector('.container');
    container.innerHTML = html;
}

renderUsers();
