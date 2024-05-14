function submitForm(formData) {
    fetch('/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        // Display the processed data

        const paragraphs = data.message.split('\n');
        let htmlContent = '';
        for (const paragraph of paragraphs) {
            htmlContent += `<p class="text-base font-light leading-relaxed mt-0 mb-4 text-copper-canyon-950">${paragraph}</p>`;
        }

        document.getElementById('upload-form-response').innerHTML = htmlContent;
        // Show the "Try Again" button
        document.getElementById('top-separator').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
}
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('upload-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);
        submitForm(formData);

    });

    // Add event listener for the "Try Again" button
    document.getElementById('try-again-button').addEventListener('click', function(event) {
        event.preventDefault();
        // Set the value of the hidden input field to indicate "Try Again"
        document.getElementById('tryAgainInput').value = '1';
        // Submit the form
        var formData = new FormData(document.getElementById('upload-form'));
        submitForm(formData);
    });
});
