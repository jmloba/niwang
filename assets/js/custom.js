$(document).ready(function(){
 
  $('.btn-email-id').on('click',function(e){
    e.preventDefault();
    btn_id  = $(this).attr('btn-id');
    email_to  = $(this).attr('data-email');
    $('#id_email_to').html(email_to);

  }); /* email_respose_btn */



  $('#ajax_student_btn1').on('click',function(e){
    e.preventDefault();
    console.log('btn-pressed just pressed')
    let xhr = new XMLHttpRequest();
    // prepare the request
    xhr.open('GET', '/assets/data/message.txt',true)
    // send request
    xhr.send();
    xhr.onload = () =>{
      if (xhr.status === 200){
        let data = xhr.responseText
        console.log(data)
        displayparagraph(data);
      }
    }

  });
  

  $('.remove-student').on('click',function(e){
    e.preventDefault();
    
    url= $(this).attr('data-url');
    console.log ('passed url is : ', url)
    $.ajax({
      type:'GET',
      url:url,
      success:function(response){
          // console.log(response)
          if (response.status=='success'){
            document.getElementById("student-"+response.id).remove()
            swal(response.status,response.message,'success')
          }
      }
    })
  });

  let displayparagraph=(data) =>{
    let htmlTemplate = `<p class="displayblock">${data}</p>`;
    console.log (htmlTemplate);
    document.querySelector('#text-display-here').innerHTML=htmlTemplate;
  }


}); /* end document */


