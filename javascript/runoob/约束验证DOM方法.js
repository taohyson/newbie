	function myFunction() {
	    var inpObj = document.getElementById("id1");
	    if (inpObj.checkValidity() == false) {
	        document.getElementById("demo").innerHTML = inpObj.validationMessage;
	    }
	}