const http = require('http');
var fs = require('fs');
const hostname = '127.0.0.1';
const port = 3000;
const { exec } = require('child_process');
let test;
exec('python3 middleware.py', (err, stdout, stderr) => {
  if (err) {
    return;
  }
  test = stdout;
});

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    // res.end(test);
    fs.readFile(__dirname + "/html/node_test.html", function(err, data){
      response.end(data);
  });
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});