
$('#add-recipe-btn').on('click',function(e){
  e.preventDefault();

  var recipe = document.getElementById('id_recipe').value
  var name = document.getElementById('id_name').value
  var directions = document.getElementById('id_directions').value
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  console.log('recipe : ', recipe)
  console.log('name : ', name)
  console.log('directions : ', directions)
    // from form = add hidden input above button
  var url = document.getElementById('add_recipe_url').value

  console.log('values from page : ',recipe,name, directions,csrf_token)
  $.ajax({
    type: 'POST',
    url : url,
    data : {
      'recipe': recipe, 
      'name': name, 
      'directions':directions, 
      'csrfmiddlewaretoken':csrf_token,
      },
      success : function(data){
        console.log('url', url)
        if( response.status =='success'){
          

            html ='<tr id="recipe-'+response.id+'"><td>'+response.recipe+'</th><td>'+response.name+'</td><td>'+response.directions+'</td><td><a href="#" class="remove_recipe_item" data-url="/app_forms/remove_recipe/'+response.id+'">Remove</a></td></tr>'

            $('.recipe-list').append(html)
            // reset the form 
            document.getElementById('add-recipe-form').reset()




        }
    }
  });  
      


});



$(document).on('click','.remove_recipe_item', function(e){
  e.preventDefault();  
  url= $(this).attr('data-url');
  console.log ('passed url is : ', url)
  $.ajax({
    type:'GET',
    url:url,
    success:function(response){
        // console.log(response)
        if (response.status=='success'){
          document.getElementById("recipe-"+response.id).remove()
          // swal(response.status,response.message,'success')
        }
    }
  })


});
