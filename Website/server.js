const http = require('http');
const fs = require('fs');
const path = require('path');

// Define the port and host to run the server
const PORT = 9000;
const HOST = '0.0.0.0';  // This makes the server accessible to all devices on the same network

// Create an HTTP server
const server = http.createServer((req, res) => {
    const filePath = path.join(__dirname, 'index.html');
    
    if (req.url === '/') {
        fs.readFile(filePath, (err, content) => {
            if (err) {
                res.writeHead(500);
                res.end('Error serving the HTML file.');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(content, 'utf-8');
            }
        });
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 - Not Found');
    }
});

// Start the server and listen on all network interfaces
server.listen(PORT, HOST, () => {
    console.log(`Server is running on http://${HOST}:${PORT}`);
});
