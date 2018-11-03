function f(x)  
    print("function")  
    return x*2   
end  
for i=1,f(5) do
	print(i)  
end  

days = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}  
for i,v in ipairs(days) do 
	print(v)
end   