function create_new_row(row_to_copy_id, new_data) {
    let canvas_row = document.getElementById(`${row_to_copy_id}`).cloneNode(true)
    let schema_id = new_data.text["schema_id"]
    let ins_before_first_row = document.getElementById(`data_row_file_id_${schema_id - 1}`)
    let file_field = canvas_row.querySelector("#file_id_field")
    let file_created_field = canvas_row.querySelector("#file_created_field")
    let status_ready = canvas_row.querySelector("#status_id_")
    let button = canvas_row.querySelector("#download_button_id_")
    let href = canvas_row.querySelector("#download_href_id_")


    file_field.innerText = schema_id
    file_field.removeAttribute("id")


    file_created_field.innerText = format_date(Date.parse(new_data.text["created"]))
    file_created_field.innerText = format_date(Date.parse(new_data.text["created"]))
    file_created_field.removeAttribute("id")
    status_ready.id = `status_id_${schema_id}`
    canvas_row.id = `data_row_file_id_${schema_id}`
    button.id = `download_button_id_${schema_id}`
    href.id = `download_href_id_${schema_id}`

    if (ins_before_first_row === null) {
        let table_body = document.getElementById('main_table_body')
        table_body.appendChild(canvas_row)
    } else {
        ins_before_first_row.before(canvas_row)

    }
}

function format_date(new_date) {
    let object_date = new Date(new_date).toLocaleString("en-GB")
    object_date = object_date.slice(0, 17)
    object_date = object_date.replace(",", "")
    return object_date
}

function generate_rows() {
    const XHR = new XMLHttpRequest()
    const FD = new FormData(document.getElementById("data_generation_form"))
    XHR.addEventListener("load", (event) => {
        let data = JSON.parse(event.target.responseText)
        create_new_row("empty_row", data)
    });

    XHR.addEventListener("error", (event) => {
        alert('Oops! Something went wrong.');
    });
    const url = document.URL

    XHR.open("POST", `${url}` + `/generate_data`, true);

    XHR.send(FD);
}

