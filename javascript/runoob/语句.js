function onLoad(argument) {
	var demo = document.getElementById('demo');
	var my = document.getElementById('my');

	console.info(onLoad.name, Date(), "INFO", demo.innerHTML, my.innerHTML);

	demo.innerHTML = '语句';
	my.innerHTML = '语句';
}