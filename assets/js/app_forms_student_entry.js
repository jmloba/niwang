


$('#add-student-btn').on('click',function(e){
  e.preventDefault();
    let name = $('#name-id').val()
  let email = $('#email-id').val()
  let course = $('#course-id').val()
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  let url= $(this).attr('data-url');
  console.log('name', name)
  console.log('email', email)
  console.log('course', course)
  
  if (name==''){
    swal('Required','please enter name','error')
  }else if (email==''){
    swal('Required','please enter Email','error')
  }else if(course==''){
    swal('Required','please enter Course','error')
  }
  else{
    mydata={'name':name, 'email':email,'course':course,'csrfmiddlewaretoken':csrf_token, }


  $.ajax( {
    type : 'POST',
    url: url,
    data : mydata,
    success: function(response){
      if( response.status =='success'){
        html='<tr id="stud-'+response.id+'"><td>'+response.id+'</td><td>'+response.name+'</td><td>'+response.email+'</td><td>'+response.course+'</td><td><button class="btn btn-danger btn-sm btn-delete-student" data-url="/app_forms/remove_student/'+ response.id +'">Delete</button> </button>&nbsp;  &nbsp;  &nbsp;<button class="btn btn-info btn-sm btn-edit-student"data-url="/app_forms/edit_student/'+response.id+'" >Edit</button></td></tr>'

        $('.student-list').append(html)
        // reset the form 
        document.getElementById('add-student-form').reset()
        }else  if (response.status=='Unable to save'){
          console.log('unable to save***')
          swal(response.status,"check Email ",'info')
        }

    } // success end
  }); // ajax end
};  

});

$(document).on('click','.btn-edit-student', function(e){  
  e.preventDefault();
  console.log('edit button pressed')
  url= $(this).attr('data-url');


  var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
  mydata={'csrfmiddlewaretoken':csrf_token, }
  mythis = this;
  console.log ('passed url is : ', url)

  $.ajax({
    type:'POST',
    url:url,
    data:mydata,
    success:function(response){
        console.log('response from views: edit_student')
        if (response.status=='success'){
          console.log('id is :', response.id)
          console.log('name', response.name)
          console.log('email', response.email)
          console.log('course', response.course)

          $('#name-id').val(response.name);
          $('#email-id').val(response.email);
          $('#course-id').val(response.course);

          // document.getElementById("stud-"+response.id).remove()
          // $(mythis).closest('tr').fadeOut()
          // swal(response.status,response.message,'success')
        } 
    }
  })
});  


$(document).on('click','.btn-delete-student', function(e){
  e.preventDefault();  
  console.log('delete student ***')
  url= $(this).attr('data-url');
  mythis = this;
    console.log ('passed url is : ', url)
    $.ajax({
      type:'GET',
      url:url,
      success:function(response){
          // console.log(response)
          if (response.status=='success'){
            // document.getElementById("stud-"+response.id).remove()
            $(mythis).closest('tr').fadeOut()
            // swal(response.status,response.message,'success')
          } 
      }
    })
  
});
$('#app_forms-student-entry').on('click',function(e){
  e.preventDefault();
  console.log('appforms entry save jvoen')

  let mname = $('#name-id').val();
  let memail = $('#email-id').val();
  let mcourse = $('#course-id').val();
  

  console.log('name :'+ mname);
  console.log('email :'+ memail);
  console.log('course :'+ mcourse);
  if (mname== '' ){
    
    swal("Failed", "Please enter name", "error") 

  } else
  if (memail==''){
    swal("Failed", "Please enter email", "error") 
  }else
  if (mcourse==''){
    swal("Failed", "Please enter course", "error") 
  }else{
    // swal("success", "ready to save ", "success")
    my_data = {
      name:mname,
      email:memail, 
      course: mcourse,
     
    }
   
  }


});

