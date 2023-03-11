function get_form(id) {
    let form = document.getElementById(id)
}

function count_columns_elements() {
    return document.getElementsByClassName("border_style").length
}

let counter = 0

function create_column() {
    let column_count = count_columns_elements()
    let insert_element = document.getElementById("append_to")
    let column = document.getElementById("column_insert")
    let value = column.querySelector('.text-capitalize').value

    let new_column = column.cloneNode(true)
    let new_column_id = new_column.id
    new_column_id = new_column_id + "_" + counter
    new_column.id = new_column_id

    let order_element = column.querySelector(".order_value")
    let new_order_element = new_column.querySelector(".order_value")


    counter++;
    if (order_element.value !== '') {
        new_order_element.value = order_element.value
    } else {
        new_order_element.value = column_count
    }
    new_column.querySelector('.text-capitalize').value = value
    new_column.style.backgroundColor = '#f2f2f2'
    insert_element.appendChild(new_column)
}


function send_form_data(form) {
    e.preventDefault()
    const FData = new FormData(form)
    console.log(FData)
    return 1
}


function sendData() {
    const XHR = new XMLHttpRequest();
    const form = document.getElementById("schema_form_id");
    // Bind the FormData object and the form element
    const FD = new FormData(form)
    let FormatedData = new FormData()
    // for (let pair of FD.entries()) {
    //     console.log(pair[0] + ": " + pair[1]);
    // }
    let counter = 0
    let field_index = 0
    let formated = {}
    let lst_of_fields = []
    let table_options = {}
    let fields = []
    let field_repr = {}
    for (let data_part of FD.entries()) {
        counter++;
        if (counter === 1){
            FormatedData.set(data_part[0],data_part[1])
        }
        if (counter <= 4 && counter > 1) {
            table_options[data_part[0]] = data_part[1]
        }
        if (counter > 4){
            field_index ++;
            field_repr[data_part[0]] = data_part[1]
            if (field_index === 4){
                fields.push(field_repr)
                field_repr = {}
                field_index = 0;
            }
        }
    }
    FormatedData.set('table_options', JSON.stringify(table_options))
    FormatedData.set('fields', JSON.stringify(fields))
      for (let data_part of FormatedData.entries()) {
          console.log(data_part[0] + "|" + data_part[1])
      }
    // Define what happens on successful data submission
    XHR.addEventListener("load", (event) => {
        alert(event.target.responseText);
    });
    // Define what happens in case of error
    XHR.addEventListener("error", (event) => {
        alert('Oops! Something went wrong.');
    });

    // Set up our request
    XHR.open("POST", "http://localhost:8000/schemas/create_schema", false);

    // The data sent is what the user provided in the form
    XHR.send(FormatedData);
}


function new_submit() {
    // Get the form element
    const form = document.getElementById("schema_form_id");

// Add 'submit' event handler
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        sendData();
    });
}

// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         let cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             let cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }