

$('#ajaxtutor-api-btn').on('click',function(e){
  e.preventDefault();
  console.log('processing for api button' );
  let xhr = new XMLHttpRequest();
  // prepare the request
  xhr.open('GET', 'https://jsonplaceholder.typicode.com/users',true)
  xhr.send();
  // process request
  xhr.onload = () =>{
    if (xhr.status === 200){
      let data = xhr.responseText
      console.log(data)
      console.log(typeof(data))
      let users =JSON.parse(data)
      console.log(users);
      displayApiData(users)

    }
  }

});


let displayApiData=(users)=>{
  let htmlTemplate='';
  for ( let user of users ){
    htmlTemplate+=
    `<ul class="list-group mt-1">
      <li class='list-group-item'>
        ID : <span >${user.id}</span>
        <ul>
          <li>Name : <span >${user.name}</span></li>
          <li>Email: <span >${user.email}</span></li>
          <li>Street: <span >${user.address.street}</span></li>
          <li>City: <span >${user.address.city}</span></li>
        </ul>
      </li>
    </ul>`
  }
  document.querySelector('#ajaxtutor-api-card').innerHTML=htmlTemplate;
}

  // ********************************************
  $('#ajaxtutor-json-btn').on('click',function(e){
    e.preventDefault();
    console.log('processing for json button' );
    let xhr = new XMLHttpRequest();
    // prepare the request
    xhr.open('GET', '/assets/data/mobile.json',true)
    // send request
    xhr.send();
    // process request
    xhr.onload = () =>{
      if (xhr.status === 200){
        let data = xhr.responseText
        console.log(data)
        console.log(typeof(data))
        let mobile=JSON.parse(data)
        console.log(mobile)
        displayJsonData(mobile)
      }
    }
  });
let displayJsonData=(mobile) =>{
  let htmlTemplate='';
  htmlTemplate=`
  <ul class='list-group mt-1 d-flex'>
    <li  class='list-group-item'>ID : <span >${mobile.id}</span></li>
    <li  class='list-group-item'>Brand : <span >${mobile.brand}</span></li>
    <li  class='list-group-item'>Color : <span >${mobile.color}</span></li>
    <li  class='list-group-item'>Price :<span > ${mobile.price}</span></li>
  </ul>`
  document.querySelector('#ajaxtutor-json-card').innerHTML=htmlTemplate;
}



  // ********************************************
// display text data
$('#ajaxtutor-text-btn').on('click',function(e){
  e.preventDefault();
  console.log('jvoen')
  let xhr = new XMLHttpRequest();
  // prepare the request
  xhr.open('GET', '/assets/data/message.txt',true)
  // send request
  xhr.send();
  // process request
  xhr.onload = () =>{
    if (xhr.status === 200){
      let data = xhr.responseText
      console.log(data)
      displayTextdata(data);
    }
  }
});
let displayTextdata=(data) =>{
  let htmlTemplate = `<p>${data}</p>`;
  console.log (htmlTemplate);
  document.querySelector('#ajaxtutor-text-card').innerHTML=htmlTemplate;
}







