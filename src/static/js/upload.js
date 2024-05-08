document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '');

        xhr.onload = function() {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                document.getElementById('upload-form-response').innerHTML = response.message;
            } else {
                document.getElementById('upload-form-response').innerHTML = 'Error uploading file';
                console.error('Upload failed:', xhr.statusText);
            }
        };

        xhr.onerror = function(error) {
            console.error('Network error:', error);
            document.getElementById('upload-form-response').innerHTML = 'Network Error';
        };

        xhr.send(formData);
    });
});
