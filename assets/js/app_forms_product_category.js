


$('#btn-categ-save').on('click',function(e){
  e.preventDefault();
  // var name = document.getElementById('id-name').value
  let name = $('#id-name').val();
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');

  console.log('button save clicked \n name:'+name)
  $.ajax({
    type: 'POST',
    url : url,
    data : {
      'name': name, 
      'csrfmiddlewaretoken':csrf_token,
      },

      success : function(data){
        console.log('url', url)
        if( data.status =='Saved'){
          html="<tr><th scope='row'>"+data.id+"</th><td>"+data.name+"</td><td><button class='btn btn-warning btn-sm btn-categ-edit' data-sid='"+data.id+"'><i class='bi bi-pen'></i></button>&ensp;&ensp;<button class='btn btn-danger btn-sm'data-sid='"+data.id+"' id='btn-categ-delete' data-url='/app_forms/category_delete/' '><i class='bi bi-trash3'></i></button></td></tr>'"
          $('#tbody').append(html)
            // reset the form 
          document.getElementById('category-form').reset()




        }
    }
  }); 
}); 

$('#tbody').on('click','#btn-categ-delete', function(e){
  e.preventDefault();  
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



  
})  