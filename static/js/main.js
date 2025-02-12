document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#diabetes-form');
    const submitButton = document.querySelector('#predict-button');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission
        submitButton.innerHTML = 'Processing...'; // Show loading spinner
        submitButton.disabled = true; // Disable button

        // Use Fetch API to send form data to backend
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
        })
            .then((response) => response.text())
            .then((html) => {
                document.body.innerHTML = html; // Replace the page with server response
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('An error occurred while processing your request.');
            })
            .finally(() => {
                submitButton.innerHTML = 'Submit'; // Reset button text
                submitButton.disabled = false; // Re-enable button
            });
    });
});


// static/js/heart-disease.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#heart-disease-form');
    const submitButton = document.querySelector('#predict-button');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        
        // Show loading state
        submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing...';
        submitButton.disabled = true;

        // Form submission
        const formData = new FormData(form);
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.text())
        .then(html => {
            document.body.innerHTML = html;
            
            // Reinitialize any JavaScript listeners on the new content
            initializeFormListeners();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing your request. Please try again.');
        })
        .finally(() => {
            // Reset button state
            submitButton.innerHTML = 'Predict Risk';
            submitButton.disabled = false;
        });
    });

    function initializeFormListeners() {
        // Re-attach event listeners to the new form if needed
        const newForm = document.querySelector('#heart-disease-form');
        if (newForm) {
            newForm.addEventListener('submit', handleSubmit);
        }
    }
});

// Helper function to show alerts
function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show mt-3`;
    alertDiv.role = 'alert';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;

    const form = document.querySelector('form');
    form.insertBefore(alertDiv, form.firstChild);

    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}
