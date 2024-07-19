
$('#btn-form-save').on('click',function(e){
    e.preventDefault();
  // console.log ('button save click')
  output=''
  let sid = $('#stuid').val() // coming from hidden 

  let name = $('#id-name').val()
  let email = $('#id-email').val()
  let course = $('#id-course').val()
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()


  mythis = $(this)
  if (name==''){
    swal('Please enter Name','required','error')
  }else if(email==''){
    swal('Please enter Email','required','error')
  } else if(course==''){
    swal('Please enter Course','required','error')
  } else {
    // console.log ('name:',name)
    // console.log ('email:',email)  
    // console.log ('course:',course)

    // create student
    url= $(this).attr('data-url');
    mydata={
      stuid:sid, // cming from hidded
      name:name, 
      email:email,
      course:course, 
      'csrfmiddlewaretoken':csrf_token,
    };

    $.ajax({
      url : url,
      type : 'POST',
      data : mydata,
      // returned whole list
      success:function(data){

        console.log('status:',data.status)
        // adding all record from list   
        x = data.student_data
        if (data.status=='Saved'){

          console.log('sending data...')

          for (i=0; i<x.length; i++){
            output +="<tr><td>"+x[i].id+
            "</td><td>"+x[i].name+
            "</td><td>"+x[i].email+
            "</td><td>"+x[i].course+
            "</td>  <td><input type='button'  class='btn  mb-1 btn-warning btn-edit-desphixs' value='Edit'data-url='/app_forms/desphixs_edit_student/' data-sid='"+x[i].id+"'>&ensp;&ensp;<input type='button'  class='btn  mb-1 btn-danger btn-delete-desphixs' value='Delete' data-url='/app_forms/desphixs_delete_student/' data-sid='"+x[i].id+"'></td></tr>"
          }
          $('#tbody').html(output)
          // $('#form')[0].reset()
          document.getElementById('form').reset()
        }
      }


      
    });
  }
});

$('#tbody').on('click','.btn-delete-desphixs', function(e){
  e.preventDefault();  
  console.log('record button delete')
  let id = $(this).attr("data-sid")
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');
  console.log ('id is   : ', id)
  mydata= {'sid':id ,
  'csrfmiddlewaretoken':csrf_token,}
  mythis = $(this)

  $.ajax({
    url:url,
    method :"POST",
    data : mydata,
    
    success:function(data){
      console.log(data)
      if (data.status==1){
        console.log('student deleted')
        $(mythis).closest("tr").fadeOut()
        
          // swal(response.status,response.message,'success')
        }
        if (data.status==0)

        {
          console.log('student --- unable to deleted')
        }

    }
  })


});

//editing student
$('#tbody').on('click','.btn-edit-desphixs', function(e){
  e.preventDefault();  
  console.log('edit button pressed')

  let id = $(this).attr("data-sid") // taken from table
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');
  mydata= {'sid':id ,
  'csrfmiddlewaretoken':csrf_token,}
  mythis = $(this)
  console.log ('edit mode --> id is   : ', id)

  $.ajax({
    url:url,
    method :"POST",
    data : mydata,
    
    success:function(data){
      console.log(data)
      $('#stuid').val(data.id) 
     $('#id-name').val(data.name)
      $('#id-email').val(data.email)
      $('#id-course').val(data.course)
     
     

    }
  })



});
