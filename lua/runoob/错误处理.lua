local function add(a,b)
   assert(type(a) == "number", "a ����һ������")
   assert(type(b) == "number", "b ����һ������")
   return a+b
end
add(10,20)

pcall(function(i) print(i) end, 33)
pcall(function(i) print(i) error('error..') end, 33)
xpcall(function(i) print(i) error('error..') end, function() print(debug.traceback()) end, 33)

function myfunction ()
   n = n/nil
end

function myerrorhandler( err )
   print( "ERROR:", err )
end

status = xpcall( myfunction, myerrorhandler )
print( status)