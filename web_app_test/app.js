const http = require('http');
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');

  var { exec } = require('child_process');
  if (req.url === '/exec/:resolucao/:title') {
    var test;
    var resolucao = req.params.resolucao;
    var title = req.params.title;
    exec('python3 ../middleware.py '+resolucao+' "'+title+'" ', (err, stdout, stderr) => {
      if (err) {
        return;
      }
      test = JSON.parse(stdout);
      console.log(test.title);
      // res.write('<h1>'+ test.title +'</h1>');
      // res.write('<h1>'+ test.title +'</h1>');
    });
  } else if (req.url === '/sobre') {
    res.write('<h1>Sobre</h1>');
  } else {
    res.write('<h1>Página não encontrada :(</h1>');
  }

});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});