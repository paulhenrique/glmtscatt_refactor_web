
const http = require('http');
var express = require('express');
var fs = require('fs');
const hostname = '127.0.0.1';
const port = 3000;
var app = express();
var { exec } = require('child_process');

app.get("/", (req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.send("Entre com um valor de resolução e título para execução");
});

app.use("/exec/:sample/:title/:wl/:axicon", (req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  res.setHeader('Access-Control-Allow-Credentials', true);
  let sample = req.params.sample;
  let title = req.params.title;
  let wl = req.params.wl;
  let axicon = req.params.axicon;
  var python_code;
  var python_code_text;
  var command = 'python3 ../middleware.py ' + sample + ' ' + title + ' ' + wl + ' ' + axicon;
  var path = '../tmp.json'; i
  exec(command, (err, stdout, stderr) => {
    if (err) {
      return;
    }

    python_code = JSON.parse(stdout);
    python_code_text = JSON.stringify(python_code);
    res.end(python_code_text);
  });

});
app.listen(port, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
