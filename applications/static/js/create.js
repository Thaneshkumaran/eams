
function create(url) {
    let myForm = document.getElementById("myform"); 
    let formData = new FormData(myForm);
    fetch(url,{
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.redirect_url;
        } else {
            alert("Form submission failed.");
        }
    })
    .catch(error => {
        console.error("Error submitting form:", error);
    });
 }
