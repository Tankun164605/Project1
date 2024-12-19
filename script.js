document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("form");
    const usernameField = document.getElementById("username");
    const passwordField = document.getElementById("password");

    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            // Reset the error messages
            usernameField.setCustomValidity('');
            passwordField.setCustomValidity('');

            if (!usernameField.value) {
                e.preventDefault();
                usernameField.setCustomValidity('Please enter your username!');
            }
            if (!passwordField.value) {
                e.preventDefault();
                passwordField.setCustomValidity('Please enter your password!');
            }
        });
    }
});