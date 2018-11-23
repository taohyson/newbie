var fs=require('fs');
fs.readFile('教程.js', function(err, data) {
	if (err) return console.error(err);
	console.log(data.toString());
});
