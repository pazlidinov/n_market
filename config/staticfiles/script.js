let password_shower = document.querySelectorAll(".auth-password_shower")

password_shower.forEach(shower => {
    shower.addEventListener("click", () => {
        shower.firstElementChild.classList.toggle("fa-eye")
        shower.firstElementChild.classList.toggle("fa-eye-slash")
        input = shower.previousElementSibling
        input.type == "password" ? input.type = "text" : input.type = "password";
    })
});