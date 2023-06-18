// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the form element
    const form = document.querySelector("#myForm");
  
    // Add an event listener for form submission
    form.addEventListener("submit", async function (event) {
      event.preventDefault();
  
      // Perform additional validation if needed
      if (!additionalValidation()) {
        return;
      }
  
      // Disable the submit button to prevent multiple submissions
      const submitButton = form.querySelector('button[type="submit"]');
      submitButton.disabled = true;
  
      try {
        // Get the form data
        const formData = new FormData(form);
  
        // Convert form data to JSON object
        const jsonData = convertFormDataToJson(formData);
  
        // Send form data to the server
        const response = await submitForm(jsonData);
  
        // Handle the form submission response
        handleFormSubmissionResponse(response);
      } catch (error) {
        // Handle any errors that occurred during the form submission
        displayErrorMessage("An error occurred. Please try again later.");
      } finally {
        // Re-enable the submit button
        submitButton.disabled = false;
      }
    });
  
    // Additional custom JavaScript code
    additionalCustomLogic();
  
    // Perform additional validation if needed
    function additionalValidation() {
      // Get the form fields
      const firstNameInput = form.querySelector("#firstName");
      const lastNameInput = form.querySelector("#lastName");
      const emailInput = form.querySelector("#email");
      const messageInput = form.querySelector("#message");
  
      // Validate First Name
      const firstName = firstNameInput.value.trim();
      if (firstName === "") {
        displayErrorMessage("First name is required");
        return false;
      }
  
      // Validate Last Name
      const lastName = lastNameInput.value.trim();
      if (lastName === "") {
        displayErrorMessage("Last name is required");
        return false;
      }
  
      // Validate Email
      const email = emailInput.value.trim();
      if (email === "") {
        displayErrorMessage("Email is required");
        return false;
      }
  
      // Validate Message
      const message = messageInput.value.trim();
      if (message === "") {
        displayErrorMessage("Message is required");
        return false;
      }
  
      // Update UI to show validation feedback if needed
      updateFieldValidationStatus(firstNameInput, true);
      updateFieldValidationStatus(lastNameInput, true);
      updateFieldValidationStatus(emailInput, true);
      updateFieldValidationStatus(messageInput, true);
  
      // Return true if all fields are valid, false otherwise
      return true;
    }
  
    // Update UI to show validation feedback if needed
    function updateFieldValidationStatus(field, isValid) {
      // Add your logic to update the UI and display validation feedback for the field
      // ...
    }
  
    // Function to convert form data to JSON object
    function convertFormDataToJson(formData) {
      const jsonData = {};
  
      for (const [key, value] of formData.entries()) {
        if (jsonData.hasOwnProperty(key)) {
          if (Array.isArray(jsonData[key])) {
            jsonData[key].push(value);
          } else {
            jsonData[key] = [jsonData[key], value];
          }
        } else if (key.includes(".")) {
          const keys = key.split(".");
          let nestedObj = jsonData;
  
          for (let i = 0; i < keys.length - 1; i++) {
            const nestedKey = keys[i];
  
            if (!nestedObj.hasOwnProperty(nestedKey)) {
              nestedObj[nestedKey] = {};
            }
  
            nestedObj = nestedObj[nestedKey];
          }
  
          nestedObj[keys[keys.length - 1]] = value;
        } else {
          jsonData[key] = value;
        }
      }
  
      return jsonData;
    }
  
    // Function to submit the form data to a backend API
    async function submitForm(formData) {
      const timeoutDuration = 5000; // Timeout duration in milliseconds
  
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeoutDuration);
  
        const response = await fetch("https://analytics.ijr.marketing/submit", {
          method: "POST",
          body: JSON.stringify(formData),
          headers: {
            "Content-Type": "application/json",
          },
          signal: controller.signal,
        });
  
        clearTimeout(timeoutId);
  
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Request failed");
        }
      } catch (error) {
        if (error.name === "AbortError") {
          throw new Error("Request timed out");
        } else {
          throw new Error("Request failed");
        }
      }
    }
  
    // Example function to handle the response from the server
    function handleFormSubmissionResponse(response) {
      // Add your custom logic to handle the response
      if (response.success) {
        // Display success message
        displaySuccessMessage("Success! We've received your message!");
  
        // Perform additional actions on successful form submission
        // For example, you can access specific properties of the response object
        // and perform specific actions based on your requirements
        if (response.data) {
          // Access the 'data' property of the response and perform actions
          // ...
        }
  
        // Reset the form
        form.reset();
      } else {
        // Display error message
        displayErrorMessage(
          "Form submission failed. Please try again. If the issue persists, please email info@ijr.marketing for further assistance."
        );
  
        // Perform additional actions on form submission failure
        // For example, you can access specific properties of the response object
        // and perform specific actions based on your requirements
        if (response.errors) {
          // Access the 'errors' property of the response and perform actions
          // ...
        }
      }
    }
  
    // Example function to display a success message
    function displaySuccessMessage(message) {
      // Create a new element to display the message
      const successMessage = document.createElement("div");
      successMessage.className = "custom-success";
      successMessage.textContent = message;
  
      // Insert the message above the form
      form.insertAdjacentElement("beforebegin", successMessage);
  
      // Remove the message after a certain time
      setTimeout(function () {
        successMessage.remove();
      }, 3000);
  
      // Update UI elements
      const successHeading = document.querySelector("#successHeading");
      successHeading.textContent = "Success, we've received your message!";
  
      const successDescription = document.querySelector("#successDescription");
      successDescription.textContent =
        "Thank you for submitting the form. We will get back to you soon.";
  
      // Show a confirmation dialog
      showAlert("Success", "Success, we've received your message!");
  
      // Reset the form
      form.reset();
  
      // Scroll to a specific section
      const section = document.querySelector("#contactSection");
      section.scrollIntoView({ behavior: "smooth" });
  
      // Example: Display a hidden section with additional content
      const additionalContent = document.querySelector("#additionalContent");
      additionalContent.style.display = "block";
  
      // Example: Make an AJAX request to fetch additional data
      fetch("https://analytics.ijr.marketing/api/data")
        .then((response) => response.json())
        .then((data) => {
          // Do something with the fetched data
          console.log(data);
        })
        .catch((error) => {
          // Handle any errors that occurred during the request
          console.error(error);
        });
  
      // Redirect to another page after a delay
      setTimeout(function () {
        window.location.href = "https://analytics.ijr.marketing/thank-you";
      }, 5000);
    }
  
    // Example function to display an error message
    function displayErrorMessage(message) {
      // Create a new element to display the message
      const errorMessage = document.createElement("div");
      errorMessage.className = "custom-error";
      errorMessage.textContent = message;
  
      // Insert the message above the form
      const formContainer = document.querySelector("#formContainer");
      formContainer.insertAdjacentElement("beforebegin", errorMessage);
  
      // Remove the message after a certain time
      setTimeout(function () {
        errorMessage.remove();
      }, 5000);
  
      // Scroll to the error message for better visibility
      errorMessage.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  
    // Example function for additional custom JavaScript code
    function additionalCustomLogic() {
      // Access the form elements
      const nameInput = document.querySelector("#name");
      const emailInput = document.querySelector("#email");
      const messageInput = document.querySelector("#message");
  
      // Example: Add event listener for real-time character count
      messageInput.addEventListener("input", function () {
        const message = messageInput.value;
        const characterCount = message.length;
  
        // Update UI element with character count
        const characterCountLabel = document.querySelector("#characterCountLabel");
        characterCountLabel.textContent = characterCount + " characters";
      });
  
      // Example: Add event listener for automatic email suggestion
      nameInput.addEventListener("input", function () {
        const name = nameInput.value;
  
        // Generate email suggestion based on name
        const emailSuggestion = name.toLowerCase().replace(/\s/g, "") + "@example.com";
  
        // Update UI element with email suggestion
        const emailSuggestionLabel = document.querySelector("#emailSuggestionLabel");
        emailSuggestionLabel.textContent = emailSuggestion;
      });
  
      // Example: Add event listener for custom behavior
      const customButton = document.querySelector("#customButton");
      customButton.addEventListener("click", function () {
        // Perform additional validation if needed
        if (!additionalValidation()) {
          return;
        }
  
        // Disable the button to prevent multiple clicks
        customButton.disabled = true;
  
        // Perform AJAX request
        fetch("https://example.com/custom-action", {
          method: "POST",
          // Include any necessary headers and data
        })
          .then((response) => {
            // Handle the response
            if (response.ok) {
              // Display success message
              displaySuccessMessage("Success!");
            } else {
              // Display error message
              displayErrorMessage("An error occurred. Please try again later.");
            }
          })
          .catch((error) => {
            // Handle any errors
            displayErrorMessage("An error occurred. Please try again later.");
          })
          .finally(() => {
            // Re-enable the button
            customButton.disabled = false;
          });
      });
  
      // Perform any other additional custom logic
      // ...
    }
  
    // Example function to display a loading spinner
    function displayLoadingSpinner() {
      // Create and insert the loading spinner element
      const loadingSpinner = document.createElement("div");
      loadingSpinner.className = "loading-spinner";
      form.insertAdjacentElement("beforebegin", loadingSpinner);
  
      // Example: Show the loading spinner for a certain duration
      setTimeout(function () {
        loadingSpinner.remove();
      }, 2000);
  
      // Example: Perform some asynchronous task
      performAsyncTask()
        .then((result) => {
          // Handle the result
          console.log(result);
        })
        .catch((error) => {
          // Handle any errors
          console.error(error);
        });
  
      // Example: Access form data from the query string
      const queryParams = new URLSearchParams(window.location.search);
      const firstName = queryParams.get("firstName");
      const lastName = queryParams.get("lastName");
      const email = queryParams.get("email");
  
      // Populate the form fields with query parameter values
      if (firstName) {
        firstNameInput.value = firstName;
      }
      if (lastName) {
        lastNameInput.value = lastName;
      }
      if (email) {
        emailInput.value = email;
      }
  
      // Example: Scroll to a specific element on the page
      const scrollToElement = document.querySelector("#scrollToElement");
      scrollToElement.scrollIntoView({ behavior: "smooth" });
  
      // Example: Show a confirmation dialog
      function showAlert(title, message) {
        // Create a modal element for the dialog
        const modal = document.createElement("div");
        modal.className = "modal";
  
        // Create the dialog content
        const dialog = document.createElement("div");
        dialog.className = "modal-dialog";
  
        const titleElement = document.createElement("h2");
        titleElement.textContent = title;
  
        const messageElement = document.createElement("p");
        messageElement.textContent = message;
  
        const closeButton = document.createElement("button");
        closeButton.textContent = "Close";
        closeButton.addEventListener("click", function () {
          modal.remove();
        });
  
        // Assemble the dialog elements
        dialog.appendChild(titleElement);
        dialog.appendChild(messageElement);
        dialog.appendChild(closeButton);
  
        // Assemble the modal
        modal.appendChild(dialog);
  
        // Insert the modal into the document
        document.body.appendChild(modal);
      }
    }
  });
  