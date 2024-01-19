function validation() {
    var username = document.Formfill.Username.value;
    var password = document.Formfill.Password.value;
    var fullname = document.Formfill.Fullname.value;
    var email = document.Formfill.Email.value;
    var telephoneNo = document.Formfill.telephoneNo.value;

    // Clear any previous messages
    clearMessages();

    // Check if username is empty or less than 10 characters
    if (username === "") {
        displayErrorMessage("Enter a valid Username.");
        return false;
    }

    // Check if password is empty or doesn't meet the criteria
    if (password === "" || !isPasswordValid(password)) {
        displayErrorMessage("Enter a valid Password (at least 10 characters, with one uppercase letter, one lowercase letter, one digit, and one of these symbols: +, !, *, -).");
        return false;
    }

    if (fullname === "") {
        displayErrorMessage("Enter a valid FullName.");
        return false;
    }

    if (email === "") {
        displayErrorMessage("Enter a valid Email address.");
        return false;
    }

    if (telephoneNo === "" || !isTelNoValid(telephoneNo)) {
        displayErrorMessage("Enter a valid Telephone Number (only numbers).");
        return false;
    }

    return true;
}

function isPasswordValid(password) {
    var passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[+!*\-]).{10,}$/;
    return passwordRegex.test(password);
}

function isTelNoValid(telephoneNo) {
    var telNoRegex = /^[0-9]+$/;
    return telNoRegex.test(telephoneNo);
}

function displayErrorMessage(message) {
    var resultElement = document.getElementById("result");
    resultElement.innerHTML = "<p style='color: red;'>" + message + "</p>";
}

function clearMessages() {
    var resultElement = document.getElementById("result");
    resultElement.innerHTML = "";
}
