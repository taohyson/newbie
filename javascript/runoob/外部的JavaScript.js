function onButtonClick3(argument) {
	var x = document.getElementById('demo3');
	console.info(onButtonClick3.name, Date(), "INFO", x.innerHTML);
	x.innerHTML = '用法';
}