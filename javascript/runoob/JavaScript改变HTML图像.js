function onBulbClicked() {
	x = document.getElementById('bulb');
	console.info(arguments.callee.name, Date(), "INFO", x.src);

	if (x.src.match("bulbon")) {
		x.src = "http://www.runoob.com/images/pic_bulboff.gif";
	} else {
		x.src = "http://www.runoob.com/images/pic_bulbon.gif";
	}
	console.log(arguments.callee.name, Date(), "LOG", x.src);
}