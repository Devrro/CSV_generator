const socket = new WebSocket('ws://localhost:8000/websocket');

socket.onmessage = function (event) {
    console.log(typeof(event));
}

socket.addEventListener('open', event => {
    console.log('WebSocket connection established!');
    console.log("finished")
    socket.send(JSON.stringify({
        'command': 'join',
        'group': 'file_creation',
    }));
});

// Listen for the 'message' event, which is triggered when a message is received
socket.addEventListener('file_gen', event => {
    console.log("Done!");
    console.log(`Received message: ${event.data}`);
});

// socket.addEventListener("any", event =>{
//     console.log(`${event.data}`)
// })
// Send a message to the server

function send_to_server() {
    socket.send("Hello")
}