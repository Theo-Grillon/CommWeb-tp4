let websocket;

websocket = new WebSocket('ws://localhost:12345');

websocket.onopen=function(event){
    console.log('Connection established.');
    websocket.send('Hi server !');
}

websocket.onmessage = function(event){
    console.log('Message received : ' + event.data);
}

websocket.onclose = function(event){
    console.log('Communication ended.');
}