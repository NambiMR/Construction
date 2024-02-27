// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
function openModal() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function closeModal() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Submit form
document.getElementById("addUserForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // You can add AJAX request here to submit the form data to your backend
    // For simplicity, let's just log the form data
    var formData = new FormData(this);
    for (var pair of formData.entries()) {
        console.log(pair[0] + ': ' + pair[1]);
    }

    // Close the modal after submitting the form
    closeModal();
});
