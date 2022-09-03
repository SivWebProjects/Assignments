// CRUD - Create, Read, Update, delete
var table = document.getElementById("table");
var msg = document.getElementById("msg");

// Global variable
var row = null;

// CREATE
// Retrieving data from Form
function retrieveData() {
    //var formData = {};
    var name = document.getElementById("studentName").value;
    var id = document.getElementById("studentID").value;
    var marks = document.getElementById("studentMarks").value;
    var arr = [
        [name, id, marks]
    ];
    if (arr.includes("")) {
        return false;
    } else {
        return arr;
    }
    return arr;
}

// READ
// Data in localStorage
function readingDataFromLocalStorage(dataEntered) {
    // Storing data in Local Storage
    var name = localStorage.setItem("studentName", dataEntered[0][0]);
    var id = localStorage.setItem("studentID", dataEntered[0][1]);
    var marks = localStorage.setItem("studentMarks", dataEntered[0][2]);

    // Getting values from local storage to table
    var name1 = localStorage.getItem("studentName", name);
    var id1 = localStorage.getItem("studentID", id);
    var marks1 = localStorage.getItem("studentMarks", marks);
    var arr = [
        [name1, id1, marks1]
    ];
    return arr;
}

// Edit
function edit(td) {
    row = td.parentElement.parentElement;
    document.getElementById("studentName").value = row.cells[0].innerHTML;
    document.getElementById("studentID").value = row.cells[1].innerHTML;
    document.getElementById("studentMarks").value = row.cells[2].innerHTML;
}

// UPDATE
function update() {
    row.cells[0].innerHTML = document.getElementById("studentName").value;
    row.cells[1].innerHTML = document.getElementById("studentID").value;
    row.cells[2].innerHTML = document.getElementById("studentMarks").value;
    row = null;
}

// DELETE
function remove(td) {
    var ans = confirm("Are you sure you want to delete this record?");
    if (ans === true) {
        row = td.parentElement.parentElement;
        table.deleteRow(row.rowIndex);
    }
}

// INSERT
function insert(readData) {
    var row = table.insertRow();
    row.insertCell(0).innerHTML = readData[0][0];
    row.insertCell(1).innerHTML = readData[0][1];
    row.insertCell(2).innerHTML = readData[0][2];
    row.insertCell(3).innerHTML = `<button onclick = edit(this)>Edit</button>
                                   <button onclick = remove(this)>Delete</button>`;
}

function onSubmit() {
    var dataEntered = retrieveData();
    var readData = readingDataFromLocalStorage(dataEntered);
    console.log(readData);
    if (dataEntered === false) {
        msg.innerHTML = `<h3 style="color:red;">Please Enter Data!</h3>`;
    } else {
        if (row === null) {
            insert(readData);
            msg.innerHTML = "Data is successfully inserted.";
        } else {
            update();
            msg.innerHTML = "Data is successfully updated.";
        }
    }
}

function resetForm() {
    document.getElementById("studentName").value = "";
    document.getElementById("studentID").value = "";
    document.getElementById("studentMarks").value = "";
}
