const http = require('http');
var express = require('express');
var fs = require('fs');
const hostname = '127.0.0.1';
const port = 3000;
var app = express();
var { exec } = require('child_process');

app.get("/", (req,res) => {
	 res.setHeader('Content-Type', 'text/html');
	res.send("Entre com um valor de resolução e título para execução");

});

app.use("/exec/:sample/:title", (req, res) => {
  let sample = req.params.sample;
  let title = req.params.title;
  var python_code;
  var python_code_text;
  var command = 'python3 ../middleware.py ' + sample + ' ' + title;
  var path = '../tmp.json';

  res.setHeader('Content-Type', 'text/html');
  exec(command, (err, stdout, stderr) => {
    if (err) {
      return;
    }
    python_code = JSON.parse(stdout);
    python_code_text = JSON.stringify(python_code);

    res.write('<img src="data:image/png;base64,' + python_code.data_img + '">');
    res.write(python_code_text);
  });
  // res.json([sample, title, command, python_code, python_code_text]);
});

// const server = http.createServer((req, res) => {

//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/html');
//   var url = req.url;
//   if (url.match("exec/")) {
//     var { exec } = require('child_process');
//     var url_split = url.split("/"); //quebrando url
//     var python_code;
//     var sample = url_split[2]; //resolução do gráfico gerado
//     var title = url_split[3]; //titulo do gráfico gerado
//     //var title_rewrite = decodeURI(title);
//     exec('python3 ../middleware.py ' + sample + '', (err, stdout, stderr) => {
//       if (err) {
//         return;
//       }
//       python_code = JSON.parse(stdout);
//       var python_code_text = JSON.stringify(python_code);
//       res.write('<img src="data:image/png;base64,' + python_code.data_img + '">');
//       res.end(python_code_text);
//     });
//   }
// });
app.listen(port, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
