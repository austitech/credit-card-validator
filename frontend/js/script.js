// status element
var statusElement = document.getElementById("status");

// form input elements
var cardNumberElement = document.getElementById("card-number");
var expiryDateElement = document.getElementById("expiration-date");
var cvvElement = document.getElementById("cvv");

// submit button
var submitBtn = document.getElementById("submit-btn");

// form input values object
let inputValues = {
    cardNumber: '',
    expiryDate: '',
    cvv: ''
}

// add event listeners to form input elements
const inputOnChange = (elem, fieldName) => {
    elem.addEventListener("change", (e) => {
        inputValues[fieldName] = e.target.value;
    });
    elem.addEventListener("focus", () => {
        statusElement.innerHTML = "Pending";
        statusElement.classList.add("pending");
        statusElement.classList.remove("success");
        statusElement.classList.remove("failure")
    })
};
inputOnChange(cardNumberElement, "cardNumber");
inputOnChange(expiryDateElement, "expiryDate");
inputOnChange(cvvElement, "cvv")

// success handler function
const onSuccess = () => {
    statusElement.innerHTML = "Success";
    statusElement.classList.remove("pending");
    statusElement.classList.remove("failure")
    statusElement.classList.add("success");
}

// failure handler function
const onFailure = () => {
    statusElement.innerHTML = "Failed";
    statusElement.classList.remove("success");
    statusElement.classList.remove("pending")
    statusElement.classList.add("failure");
}

submitBtn.addEventListener("click", () => {
    let [month, year] = inputValues.expiryDate.split("/")

    let payload = {
        expiry_month: month,
        expiry_year: year,
        card_number: inputValues.cardNumber,
        cvv: inputValues.cvv
    }

    fetch("/api/v1/credit-card/validate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then((response) => {
        response.status === 200 ? onSuccess() : onFailure()
    })
    .catch((err) => {
        onFailure()
    })
})
