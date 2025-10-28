// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal
var img = document.getElementById('myImage');
var modalContent = document.querySelector('.modal-content');

// Get the <span> element that closes the modal
var closeBtn = document.querySelector('.close-btn');

// When the user clicks the image, open the modal
img.onclick = function() {
    modal.style.display = 'block';
}

// When the user clicks on <span> (x), close the modal
closeBtn.onclick = function() {
    modal.style.display = 'none';
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}