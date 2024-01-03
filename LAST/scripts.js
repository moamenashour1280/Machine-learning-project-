function previewImage(event) {
    const fileInput = event.target;
    const file = fileInput.files[0];
    const imagePreview = document.getElementById('imagePreview');

    if (!file) {
        imagePreview.innerHTML = '';
        return;
    }

    const reader = new FileReader();
    reader.onload = function(event) {
        const imageUrl = event.target.result;
        const imgElement = document.createElement('img');
        imgElement.src = imageUrl;
        imgElement.classList.add('previewImage');
        imagePreview.innerHTML = '';
        imagePreview.appendChild(imgElement);
    };
    reader.readAsDataURL(file);
}

function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select an image file');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const predictionResult = document.getElementById('predictionResult');
        predictionResult.innerHTML = `Prediction: ${JSON.stringify(data)}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error occurred. Please try again.');
    });
}
