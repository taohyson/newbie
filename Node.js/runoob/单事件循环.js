var events=require('events');

var eventEmitter=new events.EventEmitter();
var connectHandler=function connected(argument) {
	console.log('success to connection');
	eventEmitter.emit('data');
};
eventEmitter.on('connection', connectHandler);
eventEmitter.on('data', function received(argument) {
	console.log('success to received');
});
eventEmitter.emit('connection');
console.log('game over')