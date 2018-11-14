function onDigitClick() {
	var digit = document.getElementsByTagName('digit');
	console.info(onDigitClick.name, Date(), "INFO", digit.value);
	if (""==digit.value || isNaN(digit.value)){
		console.error(onDigitClick.name, Date(), "ERROR", digit.value + "不是数字");
	}
}