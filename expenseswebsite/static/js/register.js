const usernameField = document.querySelector('#usernameField');
const feedBackArea = document.querySelector('.invalid_feedback')
const emailField = document.querySelector('#emailField')
const passwordField = document.querySelector("#passwordField")
const emailFeedBackArea = document.querySelector(".emailFeedBackArea")
const usernamesuccessOutput = document.querySelector(".usernamesuccessOutput")
const emailsuccessOutput = document.querySelector(".emailsuccessOutput")
const showPasswordToggle = document.querySelector(".showPasswordToggle")
const submitBtn = document.querySelector('.submit-btn')


const handleToggleInput = (e) => {
    if (showPasswordToggle.textContent === "SHOW") {
        showPasswordToggle.textContent = "HIDE"
        passwordField.setAttribute("type", "text")
    } else {
        showPasswordToggle.textContent = "SHOW"
        passwordField.setAttribute("type", "password")
    }
}
// THE ABOVE CODE WILL WORK WITH THIS BELOW CODE ASLO 
// var state = false
// const toggle = () => {
//     if (state) {
//         passwordField.setAttribute("type", "password")
//         state = false
//     }
//     else {
//         passwordField.setAttribute("type", "text")
//         state = true
//     }
// }

showPasswordToggle.addEventListener("click", handleToggleInput)

emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value

    emailsuccessOutput.textContent = `Checking  ${emailVal}`

    emailField.classList.remove('is-invalid')
    emailFeedBackArea.style.display = 'none'


    if (emailVal.length > 0) {
        emailsuccessOutput.style.display = "block";
        fetch("/authentication/validate-email", {
            body: JSON.stringify({ email: emailVal }),
            method: "POST",
        })

            .then(res => res.json())
            .then(data => {

                emailsuccessOutput.style.display = "none";
                if (data.email_error) {
                    // submitBtn.setAttribute('disabled', 'disabled')
                    emailField.classList.add('is-invalid')
                    emailFeedBackArea.style.display = 'block'
                    emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`
                    submitBtn.disabled = true
                } else {
                    submitBtn.removeAttribute('disabled')
                }
            })
    }
})


usernameField.addEventListener("keyup", (e) => {

    const usernameVal = e.target.value
    usernamesuccessOutput.style.display = "block";
    usernamesuccessOutput.textContent = `Checking  ${usernameVal}`

    usernameField.classList.remove('is-invalid')
    feedBackArea.style.display = 'none'


    if (usernameVal.length > 0) {
        fetch("/authentication/validate-username", {
            body: JSON.stringify({ username: usernameVal }),
            method: "POST",
        })
            .then(res => res.json())
            .then(data => {
                usernamesuccessOutput.style.display = "none";
                if (data.username_error) {
                    usernameField.classList.add('is-invalid')
                    feedBackArea.style.display = 'block'
                    feedBackArea.innerHTML = `<p>${data.username_error}</p>`
                    submitBtn.disabled = true
                } else {
                    submitBtn.removeAttribute('disabled')
                }
            })
    }
})