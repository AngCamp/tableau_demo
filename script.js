document.addEventListener("DOMContentLoaded", function () {
    // Selecting elements
    const inputField = document.getElementById("userInput");
    const submitButton = document.getElementById("submitBtn");
    const resultDisplay = document.getElementById("result");

    // Event listener for button click
    submitButton.addEventListener("click", function () {
        let userInput = inputField.value;
        if (userInput.trim() === "") {
            resultDisplay.innerText = "Please enter a value!";
            return;
        }

        // Simulated response
        let simulatedOutput = "Simulated Prediction: " + (parseFloat(userInput) * 1.2).toFixed(2);
        resultDisplay.innerText = simulatedOutput;
    });
});
