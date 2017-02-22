// With http, we are creating our server.
var http = require('http');


// Here we are
http.createServer(function(request, response){
  response.writeHead(200);
  response.write("Hello world!");
  response.end();
}).listen(8080, function(){
  console.log("Listening on port 8080");
})
