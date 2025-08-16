const API_URL = '/api/employees/';
document.addEventListener('DOMContentLoaded', fetchEmployees);

function create(API_URL) {
    let myForm = document.getElementById("employeeForm");
    let formData = new FormData(myForm);

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        fetchEmployees(); 
        myForm.reset();
    })
    .catch(error => console.error("Error submitting form:", error));
}



function fetchEmployees() {
    fetch(API_URL)
    .then(res => res.json())
    .then(data => {
        let rows = '';
        data.forEach(emp => {
            rows += `
                <tr>
                    <td>${emp.employee_ID}</td>
                    <td>${emp.fname} ${emp.lname}</td>
                    <td>${emp.emp_email}</td>
                    <td>
                        <button onclick="editEmployee(${emp.employee_ID})">Edit</button>
                        <button onclick="deleteEmployee(${emp.employee_ID})">Delete</button>
                    </td>
                </tr>
            `;
        });
        document.querySelector('#employeeTable tbody').innerHTML = rows;
    });
}

function editEmployee(id) {
    fetch(API_URL + id + '/')
    .then(res => res.json())
    .then(emp => {
        let form = document.getElementById('employeeForm');
        form.fname.value = emp.fname;
        form.lname.value = emp.lname;
        form.emp_email.value = emp.emp_email;
        form.emp_pass.value = emp.emp_pass;
        form.gender.value = emp.gender;
        form.age.value = emp.age;
        form.contact_add.value = emp.contact_add;

        form.onsubmit = function(e) {
            e.preventDefault();
            let formData = new FormData(form);

            fetch(API_URL + id + '/', {
                method: 'PUT',
                headers: { 'X-CSRFToken': getCookie('csrftoken') },
                body: formData
            })
            .then(() => {
                fetchEmployees();
                form.reset();
                form.onsubmit = (e) => {
                    e.preventDefault();
                    create(API_URL);
                };
            });
        };
    });
}

function deleteEmployee(id) {
    if (confirm("Are you sure you want to delete this employee?")) {
        fetch(API_URL + id + '/', {
            method: 'DELETE',
            headers: { 'X-CSRFToken': getCookie('csrftoken') }
        })
        .then(() => fetchEmployees());
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
