const container = document.querySelector('ul');

const fetchData = async () => {
  const response = await fetch('https://jsonplaceholder.typicode.com/users');
  const data = await response.json();
  return data;
};

const showUsers = async () => {
  const data = await fetchData();
  data.forEach((val) => {
    const div = getDivTag(val);
    const li = document.createElement('li');
    li.append(div);
    container.appendChild(li);
  });
};

const getDivTag = (info) => {
  const div = document.createElement('div');
  const name = info.name;
  for (let key in info) {
    const p = getParagraphTag(key, info[key]);
    div.append(p);
  }
  return div;
};

const getParagraphTag = (key, value) => {
  const p = document.createElement('p');
  let pair = '';
  if (key !== 'address' && key !== 'company') {
    pair = `${key}: ${value}`;
  } else if (key === 'address') {
    pair = `${key}: ${value.street}`;
  } else if (key === 'company') {
    pair = `${key}: ${value.name}`;
  }
  p.innerText = pair;
  return p;
};

showUsers();
