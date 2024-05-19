function submitForm(formData) {
    fetch('/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
        }
    })
        .then(response => response.json().then(data => ({ status: response.status, body: data })))
        .then(responseData => {
            document.getElementById('loading-animation').style.display = 'none';

            if (responseData.status === 200) {
                // Display the processed data
                const paragraphs = responseData.body.message.split('\n');
                let htmlContent = '';
                for (const paragraph of paragraphs) {
                    htmlContent += `<p class="text-base font-light leading-relaxed mt-0 mb-4 text-copper-canyon-950">${paragraph}</p>`;
                }
                document.getElementById('upload-form-response').innerHTML = htmlContent;
                document.getElementById('upload-form-response').style.display = 'block';
                document.getElementById('top-separator').style.display = 'block';
                document.getElementById('tryAgainInput').value = '0';
            } else {
                // Display the errors
                const errors = responseData.body.errors;
                console.log(errors)
                let errorMessage = '<ul>';
                for (let field in errors) {
                    if (errors.hasOwnProperty(field)) {
                        errorMessage += `<li>${field}: ${errors[field].join(', ')}</li>`;
                    }
                }
                errorMessage += '</ul>';
                document.getElementById('upload-form-response').innerHTML = `<div class="border border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">${errorMessage}</div>`;
                document.getElementById('upload-form-response').style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('loading-animation').style.display = 'none';
            document.getElementById('upload-form-response').innerHTML = '<p class="error">An unexpected error occurred.</p>';
            document.getElementById('upload-form-response').style.display = 'block';
            document.getElementById('top-separator').style.display = 'block';
        });
}
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('upload-form').addEventListener('submit', function (event) {
        event.preventDefault();
        var formData = new FormData(this);
        submitForm(formData);
        document.getElementById('loading-animation').style.display = 'block';

    });

    // Add event listener for the "Try Again" button
    document.getElementById('try-again-button').addEventListener('click', function (event) {
        event.preventDefault();
        // Set the value of the hidden input field to indicate "Try Again"
        document.getElementById('tryAgainInput').value = '1';
        document.getElementById('upload-form-response').style.display = 'none';
        // Submit the form
        var formData = new FormData(document.getElementById('upload-form'));
        submitForm(formData);
        document.getElementById('loading-animation').style.display = 'block';
    });
});
