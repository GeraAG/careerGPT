document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const uploadButton = document.getElementById('upload-button');
    const loadingSpinner = document.getElementById('loading-spinner');  // Add a loading spinner element
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '');

        xhr.onload = function() {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                const paragraphs = response.message.split('\n');
                let htmlContent = '<div class="relative flex py-5 items-center"><div class="flex-grow border-t border-copper-canyon-400"></div><span class="flex-shrink mx-4 text-copper-canyon-950">Ideas</span><div class="flex-grow border-t border-copper-canyon-400"></div></div>';
                for (const paragraph of paragraphs) {
                    htmlContent += `<p class="text-base font-light leading-relaxed mt-0 mb-4 text-copper-canyon-950">${paragraph}</p>`;
                }

                document.getElementById('upload-form-response').innerHTML = htmlContent;
            } else {
                let errorUpload = '<div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative"><strong class="font-bold">Error uploading file</strong></div>';

                document.getElementById('upload-form-response').innerHTML = errorUpload;
                console.error('Upload failed:', xhr.statusText);
            }
            uploadButton.disabled = false;
            loadingSpinner.style.display = 'none';
        };

        xhr.onerror = function(error) {
            console.error('Network error:', error);
            document.getElementById('upload-form-response').innerHTML = 'Network Error';
        };

        uploadButton.disabled = true;
        loadingSpinner.style.display = 'block';

        xhr.send(formData);
    });
});
