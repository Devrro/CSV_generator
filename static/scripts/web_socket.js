const socket = new WebSocket('ws://localhost:8000/websocket');

socket.onmessage = function (event) {
    let type = event.data.type
    console.log(1)
}
socket.addEventListener('open', event => {
    console.log('WebSocket connection established!');
    socket.send('Hello, server!');
});

// Listen for the 'message' event, which is triggered when a message is received
socket.addEventListener('message', event => {
    console.log("Done!");
    console.log(`Received message: ${event.data}`);
});

socket.addEventListener("any", event =>{
    console.log(`${event.data}`)
})
// Send a message to the server

function send_to_server(){
    socket.send("Hello")
}