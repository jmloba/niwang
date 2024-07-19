

$('#tbody-email-in').on('click','#btn-emailin-delete', function(e){
  e.preventDefault(); 
  let id = $(this).attr("data-sid")
  url= $(this).attr('data-url');

  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  
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
        console.log('email deleted')
        $(mythis).closest("tr").fadeOut()
        
          // swal(response.status,response.message,'success')
        }
        if (data.status==0)

        {
          console.log('student --- unable to deleted')
        }

    }
  })



}) ;   


$('#tbody-email-in').on('click','#btn-email-reply', function(e){
  e.preventDefault(); 

  let id = $(this).attr("data-sid")

  let email_from = $(this).attr("data-email")


  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');

  console.log ('id is   : ', id)
  console.log('email from :',email_from)

  mydata= {'sid':id ,
  'csrfmiddlewaretoken':csrf_token,}
  mythis = $(this)
  $('#form-data-email').val(email_from) 
  $('#email-record').val(id) 

}) ;     

$('#button-reply').on('click',function(e){
  e.preventDefault();

  var id = $('#email-record').val()
  var form_data_emailto = $('#form-data-email').val()
  var form_data_body    = $('#form-data-body').val()
  var form_data_amount  = $('#form-data-package').val()


  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');
  
  console.log('id ' , id)
  console.log('form_data_emailto  : ' , form_data_emailto)
  console.log('form_data_body     : ' , form_data_body)
  console.log('form_data_amount   : ' , form_data_amount)

  mydata= {'sid':id , 
  'csrfmiddlewaretoken':csrf_token,

  'form_data_emailto': form_data_emailto,
  'form_data_body'   : form_data_body,
  'form_data_amount' : form_data_amount

    }
  mythis = $(this)  
  $.ajax({
    url:url,
    method :"POST",
    data : mydata,
    
    success:function(data){
      console.log(data)
      if (data.status==1){
        console.log('email db is updated')
        

        location.reload(true)
        return false;

        }
        if (data.status==0) {
          console.log('student --- unable to update')

        }


    }
  })
}) ;  



