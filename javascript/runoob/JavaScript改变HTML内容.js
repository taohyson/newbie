function onContentClick() {
	x=document.getElementById('content');
	console.info(arguments.callee.name, Date(), "INFO", x.innerHTML);
	x.innerHTML='It is joke!';
}