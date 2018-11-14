for (var i=0;i<cars.length;i++)
{ 
    document.write(cars[i] + "<br>");
}

var person={fname:"John",lname:"Doe",age:25}; 
for (x in person)  // x 为属性名
{
    txt=txt + person[x];
}