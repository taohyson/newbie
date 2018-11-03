local f = loadlib("/usr/local/lua/lib/libluasocket.so", "luaopen_socket")

local f = assert(loadlib("/usr/local/lua/lib/libluasocket.so", "luaopen_socket"))
-- local f = assert(loadlib("C:\\windows\\luasocket.dll", "luaopen_socket")) -- 这是 Window 平台下
f()  -- 真正打开库