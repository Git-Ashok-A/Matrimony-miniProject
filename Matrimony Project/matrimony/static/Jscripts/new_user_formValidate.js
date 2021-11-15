function validateForm() {
    //collect form data in JavaScript variables
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;
    // var name1 = document.getElementById("fname").value;
    // var email = document.getElementById("lname").value;
    email = document.getElementById("email").value;

    //character email data validation
    if (!isNaN(email)) {
        document.getElementById("emailError").innerHTML = "**Only characters are allowed";
        return false;
    }

    //check empty password field
    if (password == "") {
        document.getElementById("message1").innerHTML = "**Fill the password please!";
        return false;
    }

    //check empty confirm password field
    if (confirm_password == "") {
        document.getElementById("message2").innerHTML = "**Enter the password please!";
        return false;
    }

    //minimum password length validation
    if (password.length < 8) {
        document.getElementById("message1").innerHTML = "**Password length must be atleast 8 characters";
        return false;
    }

    //maximum length of password validation
    if (password.length > 15) {
        document.getElementById("message1").innerHTML = "**Password length must not exceed 15 characters";
        return false;
    }

    if (password != confirm_password) {
        document.getElementById("message2").innerHTML = "**Passwords are not same";
        return false;
    } else {
        alert("Submit?");
        //document.write("JavaScript form has been submitted successfully");
        //window.location.href = "{{ url_for('home') }}"

    }
}