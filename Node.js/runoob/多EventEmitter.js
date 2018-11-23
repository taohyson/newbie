var EventEmitter = require('events').EventEmitter;
var event = new EventEmitter();
event.on('testevent', function(arg1, arg2){
	console.log('listener1',arg1,arg2);
});
event.on('testevent', function(arg1,arg2){
	console.log('listener2',arg1,arg2);
});
event.emit('testevent', 1, 2);