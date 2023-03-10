const socket = new WebSocket('ws://localhost:8000/websocket');
socket.addEventListener('open', event => {
    console.log('WebSocket connection established!');
    socket.send('Hello, server!');
});

// Listen for the 'message' event, which is triggered when a message is received
socket.addEventListener('message', event => {
    console.log(`Received message: ${event.data}`);
});
// Send a message to the server

function send_to_server(){
    socket.send("Hello")
}