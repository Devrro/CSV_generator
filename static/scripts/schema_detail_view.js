function generate_rows() {
    const XHR = new XMLHttpRequest()
    console.log(document.getElementById("data_generation_form"));
    const FD = new FormData(document.getElementById("data_generation_form"))
    XHR.addEventListener("load", (event) => {
        alert(event.target.responseText);
    });
    // Define what happens in case of error
    XHR.addEventListener("error", (event) => {
        alert('Oops! Something went wrong.');
    });
    const url = document.URL
    // Set up our request
    console.log(`${url}` + `/generate_data`)
    XHR.open("POST", `${url}` + `/generate_data`, true);

    // // The data sent is what the user provided in the form
    XHR.send(FD);
}