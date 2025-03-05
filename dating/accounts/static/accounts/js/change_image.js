let targetImageInput = document.getElementById('targetImageInput');
let targetImageImg = document.getElementById('targetImageImg');

targetImageInput.addEventListener('input', function(inputEvent) {
    let value = URL.createObjectURL(targetImageInput.files[0]);
    targetImageImg.src = value;
    targetImageImg.onload = () => URL.revokeObjectURL(value);
});