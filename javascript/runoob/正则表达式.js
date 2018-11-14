var str = "Visit Runoob!"; 
var n = str.search(/Runoob/i);
var str = "Visit Runoob!"; 
var n = str.search("Runoob");

var str = document.getElementById("demo").innerHTML; 
var txt = str.replace(/microsoft/i,"Runoob");
var str = document.getElementById("demo").innerHTML; 
var txt = str.replace("Microsoft","Runoob");

var patt = /e/;
patt.test("The best things in life are free!");
/e/.test("The best things in life are free!")

/e/.exec("The best things in life are free!");