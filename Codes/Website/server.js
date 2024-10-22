const http = require('http');
const fs = require('fs');
const path = require('path');

// Function to load fetch based on the version
async function loadFetch() {
    try {
        return (await import('node-fetch')).default; // Importing fetch dynamically for node-fetch v3.x
    } catch (error) {
        return require('node-fetch'); // Fallback for node-fetch v2.x
    }
}

(async () => {
    const fetch = await loadFetch(); // Load fetch

    const PORT = process.env.PORT || 9000; // Use environment variable or default to 9000
    const HOST = process.env.HOST || '0.0.0.0'; // Use environment variable or default to 0.0.0.0

    // Variable to store fetched data
    let sensorData = {};

    // Function to fetch sensor data
    const fetchSensorData = async () => {
        try {
            const response = await fetch('http://192.168.1.5:5000/data'); // Update the URL as necessary
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            sensorData = await response.json();
        } catch (error) {
            console.error('Error fetching data:', error.message);
        }
    };

    // Fetch sensor data every 2 seconds
    setInterval(fetchSensorData, 2000);

    const server = http.createServer((req, res) => {
        const filePath = path.join(__dirname, 'index.html');

        // Serve the HTML file on root request
        if (req.url === '/') {
            fs.readFile(filePath, (err, content) => {
                if (err) {
                    console.error('Error serving HTML file:', err);
                    res.writeHead(500, { 'Content-Type': 'text/plain' });
                    res.end('Error serving the HTML file.');
                    return;
                }
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(content, 'utf-8');
            });
        } 
        // Serve the fetched sensor data for '/data' request
        else if (req.url === '/data') {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(sensorData));
        } 
        // Handle 404 errors for other requests
        else {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('404 - Not Found');
        }
    });

    // Start the server
    server.listen(PORT, HOST, () => {
        console.log(`Server is running on http://${HOST}:${PORT}`);
    });

    // Initial fetch to get data immediately on startup
    fetchSensorData();
})();
