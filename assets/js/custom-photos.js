const alertBox = document.getElementById('alert-box')
const imgBox = document.getElementById('image-box')
const form = document.getElementById('photo-form')

const name = document.getElementById('id_name') 
const image = document.getElementById('id_image') 
const description = document.getElementById('id_description') 

const csrf=document.getElementsByName('csrfmiddlewaretoken')
console.log('csrf:', csrf)

const url = ''
const handleAlerts = (type, text) => {
  alertBox.innerHTML=
  `<div class="alert alert-${type}" role="alert">
  ${text}
</div>`
}

image.addEventListener('change',() => {
  const img_data= image.files[0]
  console.log('img_data', img_data)
  
  const url = URL.createObjectURL(img_data)
  
  imgBox.innerHTML =
   `<img src="${url}" width="50%" >`;
  console.log ('url is :' ,url)
});


form.addEventListener('submit', e =>{
  e.preventDefault;
  const fd = new FormData();
  fd.append('csrfmiddlewaretoken',csrf[0].value)
  fd.append('name', name.value)
  fd.append('description',description.value)
  fd.append('image',image.files[0])
  $.ajax({
    type: 'POST',
    url:url,
    enctype:'multipart/form-data',
    data:fd,
    success: function(response){
      console.log(response)
      const sText =`successfully saved ${response.name}`
      handleAlerts('success',sText)
      setTimeout(()=>{
        alertBox.innerHTML=''
        imgBox.innerHTML=''
        name.value=''
        description.value =''
        image.value=''

      },2000)

    },
    error:function(error){
      console.log(error)
      handleAlerts('danger','opps..something went wrong')
    },
    casche : false,
    contentType : false,
    processData: false,


  })

});