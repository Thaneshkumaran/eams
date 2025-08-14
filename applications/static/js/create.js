function create(url) {
    let myForm = document.getElementById("myform"); 
    let formData = new FormData(myForm);
    fetch(url, {
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


function read(url) {
    fetch(url, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        console.log("Fetched data:", data);
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
}


function update(url, id) {
    let myForm = document.getElementById("myform"); 
    let formData = new FormData(myForm);
    fetch(`${url}${id}/`, {
        method: 'PUT',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.redirect_url;
        } else {
            alert("Update failed.");
        }
    })
    .catch(error => {
        console.error("Error updating data:", error);
    });
}


function remove(url, id) {
    if (confirm("Are you sure you want to delete this record?")) {
        fetch(`${url}${id}/`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                alert("Deleted successfully.");
                location.reload();
            } else {
                alert("Delete failed.");
            }
        })
        .catch(error => {
            console.error("Error deleting data:", error);
        });
    }
}
