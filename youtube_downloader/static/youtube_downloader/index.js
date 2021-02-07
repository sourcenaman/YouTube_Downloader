var exampleModal = document.getElementById('exampleModal');
exampleModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var resolution = button.getAttribute('data-resolution')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var resolutionText = exampleModal.querySelector('#resolution')
  resolutionText.value = resolution
});

base_url = window.location.origin
div = document.getElementById('progress-bar')
token = div.getAttribute('data-token')
progress = 0

var myVar = setInterval(progressData, 3000);

function progressData(){
    $.ajax({
      type: 'POST',
      url: base_url + '/progress/' + token,
      success: function(data){
        progress = data.progress;
        console.log(progress);
        div.setAttribute('aria-valuenow', progress);
        div.style.width = progress + '%';
      },
      error: function(jqXHR, textStatus, errorThrown){
        clearInterval(myVar);
      }
    });
  }