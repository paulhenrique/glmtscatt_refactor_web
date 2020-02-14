const http = require('http');
var express = require('express');
var fs = require('fs');
const hostname = '127.0.0.1';
const port = 3000;
var app = express();
var spawn = require('child_process').spawn;

app.get("/", (req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.send("Entre com um valor de resolução e título para execução");
});

app.use("/exec/:sample/:title/:wl/:axicon", (req, res) => {
  // res.setHeader('Content-Type', 'text/html');
  res.setTimeout(120*60*1000, function () {
    console.log('Request has timed out.');
    res.send(408);
  });
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
  res.setHeader('Access-Control-Allow-Credentials', true);
  let sample = req.params.sample;
  let title = req.params.title;
  let wl = req.params.wl;
  let axicon = req.params.axicon;
  var command = 'python3';
  var folder = '../middleware.py';
  var args = [folder, sample, title, wl, axicon];
  command = 'python3';
  const pythonSpawn = spawn(command, args);
  pythonSpawn.stdin.setDefaultEncoding('utf-8');
  pythonSpawn.stdout.setDefaultEncoding('utf-8');

  var dataString = '';
  pythonSpawn.stdout.on('data', (data) => {
    // console.log(`pythonSpawn stdout:\n${data}`);
    dataString += data.toString();
    // res.end(JSON.parse(JSON.stringify(data.toString())));
  });
  pythonSpawn.stdout.on('end', () => {
    res.end(JSON.parse(JSON.stringify(dataString)));
  });

  pythonSpawn.stderr.on('data', (data) => {
    console.error(`pythonSpawn stderr:\n${data}`);
  });


});
app.listen(port, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
