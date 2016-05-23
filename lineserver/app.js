var express = require('express');
var fs = require('fs');
var line_array = [];
var path = process.argv[2];
var app = express();

app.get('/lines/:id', function (req, res) {

	var line_index = req.params.id;

	if (line_index > 0 && line_index <= line_array.length) {
		res.status(200).send(line_array[line_index-1]);
	}

	else {
		res.status(413).send('Index out of bounds: ' + line_index);
	}
});

// 404 error handling
app.use(function (req, res) {
	res.status(404).send('404: Page not found');
});

// Start webserver and listen on port 3000
// On start, log that the webserver has started and cache the text file in memory
// to eliminate excessive Disk IO.

app.listen(3000, function () {
	console.log('listening on port 3000');
	fs.readFile(path, function(err, f){
    	line_array = f.toString().split('\n');
    	line_array.pop();
	});
});
