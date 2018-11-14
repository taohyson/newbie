function onStyleClick(argument) {
	var x = document.getElementById('style');
	console.log(onStyleClick.name, Date(), "INFO", x.style.color);
	x.style.color = "#ff0000";
}