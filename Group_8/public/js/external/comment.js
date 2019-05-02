$( document ).ready(function() {
    //console.log(document);
    // SUBMIT FORM
      $("#userForm").submit(function(event) {
      // Prevent the form from submitting via the browser.
      event.preventDefault();
      ajaxPost();
    });
      
      
      function ajaxPost(){
        
        // PREPARE FORM DATA
        var formData = {
          comment : $("#comment").val()
        }
        
        // DO POST
        $.ajax({
        type : "POST",
        contentType : "application/json",
        url : window.location + "/TheUsualSuspects",
        data : JSON.stringify(formData),
        dataType : 'json',
        success : function(movie) {
          $("#onclick").html("<p>" + 
            "Post Successfully! <br>" +
            "--> " + movie.comment +  "</p>");
        },
        error : function(e) {
          alert("Error!")
          console.log("ERROR: ", e);
        }
      });
        
        // Reset FormData after Posting
        resetData();
   
      }
      
      function resetData(){
        $("#comment").val("");
      }
  })