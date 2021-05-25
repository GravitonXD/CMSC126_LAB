// sets the style to show the error message in the website
function error(x){
   x.style.padding = "15px";
   x.style.backgroundColor = "#EF4423";
   x.style.color = "#fff";
   x.style.borderRadius = "15px";
}

// sets the style to show the successful submisison of form message in the website
function no_error(x){
   x.style.padding = "15px";
   x.style.backgroundColor = "#74C378";
   x.style.color = "#fff";
   x.style.borderRadius = "15px";
   x.innerHTML = "Submitted Successfully";
}

// function that validates the entry in the contact us form
function validator() {
   // initializes variable names and assigns their value to corresponding entry in the html form
   var name = document.getElementById("name").value;
   var e_mail = document.getElementById("e_mail").value;
   var subject = document.getElementById("topic_request").value;
   var service = document.getElementById("service").value;
   var message = document.getElementById("message").value;
   var submission_message = document.getElementById("error_message");

   // different validation statements
   
   // name should have character length greater than 10
   if(name.length < 10) {
      error(submission_message);
      submission_message.innerHTML = "Please Enter a Valid Full Name";
      return false;
   }

   // valid e-mail should contain "@" and ".com", and should exceed 5 char length
   if(((e_mail.indexOf("@") && e_mail.indexOf(".com") == -1) && (e_mail.length < 5))) {
      error(submission_message);
      submission_message.innerHTML = "Please Enter a Valid E-mail Address";
      return false;
   }

   // subject should have character length greater than 5
   if(subject.length < 5) {
      error(submission_message);
      submission_message.innerHTML = "Please Enter a Valid Subject";
      return false;
   }

   // checks if the entry is either of the three possible valid entry, else error is shown
   if(service.toUpperCase() == "MOBILE APP" || service.toUpperCase() == "WEBSITE" || service.toUpperCase() == "BOTH"){
   } else {
      error(submission_message);
      submission_message.innerHTML = "Please Enter a 'Mobile App' or 'Website' or 'Both' in Services";
      return false;
   }

   // message should have character length greater than 20
   if(message.length < 20) {
      error(submission_message);
      submission_message.innerHTML = "Please Enter a Valid Message with atleast 20 characters";
      return false;
   }

   // If there are already no error then no_error function will run and will return true
   no_error(submission_message);
   return false;
}
