t net = require('ws');

id = 0
port = 2002
var server = new net.Server({
	        port,
	        verifyClient(info) {
			                return true;
			        }
});
server.on('listening', function() {
	        console.log('net Server listening on port %d', port)
})
server.on('error', console.log)

server.on('connection', function connection(ws, req) {
	    const address = req.connection.remoteAddress
	    console.log('Device connected: %s', address)
	    // set timeout to stop the connections
	     ws.on('error', console.log)
	     ws.on('open', function open() {
             	ws.send('CLOUD ID:' + str(id++));
             })
	     ws.on('message', function incoming(data) {
	        console.log(data);
	     })
	     ws.on('close', val => {
	        console.log(' Device disconnect: %s', address)
	     })
})
