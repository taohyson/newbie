function onParseClick() {
	var text = document.getElementById('json').value;
	obj = JSON.parse(text);
	document.getElementById("demo").innerHTML = obj.sites[1].name + " " + obj.sites[1].url;
}