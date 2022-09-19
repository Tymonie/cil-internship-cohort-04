async function fetchposts() {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com.users');
      return response.json();
      if (! response.ok) {
          throw new error(`failed to fetch post: ${response.status}`);
      }
      return response.json();
      {}
   } catch (e) {
      console.log(e);
   }
  }
  
  
  function listposts(postcontainerElementid){
      const postcontainerElement = document.getElementById
      (postcontainerElementid);{
          return;
      }
      
      fetchposts(). then(post =>{
  
      }).catch(e =>{
          console.log(e);
      })
  }
  function postElement(post) {
      const anchorElement = document.createElement('a');
      anchorElement.setAttribute
  }