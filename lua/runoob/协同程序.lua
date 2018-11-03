	-- 协同程序有点类似同步的多线程，在等待同一个线程锁的几个线程有点类似协同。（表象）
	-- 协程=模拟线程（本质）

-- coroutine_test.lua 文件
co = coroutine.create(
    function(i)
        print(i);
    end
)
 
coroutine.resume(co, 1)   -- 1
print(coroutine.status(co))  -- dead
 
print("----------")
 
co = coroutine.wrap(
    function(i)
        print(i);
    end
)
 
co(1)
 
print("----------")
 
	co2 = coroutine.create(
	    function()
	        for i=1,10 do
	            print(i)
	            if i == 3 then
	                print(coroutine.status(co2))  --running
	                print(coroutine.running()) --thread:XXXXXX
	            end
	            coroutine.yield()
	        end
	    end
	)
	 
	coroutine.resume(co2) --1
	coroutine.resume(co2) --2
	coroutine.resume(co2) --3
	 
	print(coroutine.status(co2))   -- suspended
	print(coroutine.running())
 
print("----------")


function foo (a)
    return coroutine.yield(2 * a) -- 返回  2*a 的值
end
 
co = coroutine.create(function (a , b)
    print("第一次协同程序执行输入", a, b) -- co-body 1 10
    local r = foo(a + 1)
     
    print("第二次协同程序执行输入", r)
    local r, s = coroutine.yield(a + b, a - b)  -- a，b的值为第一次调用协同程序时传入
     
    print("第三次协同程序执行输入", r, s)
    return b, "结束协同程序"                   -- b的值为第二次调用协同程序时传入
end)
        
print("main", coroutine.resume(co, 1, 10)) -- true, 4
print("main", coroutine.resume(co, "zhujw")) -- true 11 -9
print("main", coroutine.resume(co, "x", "y")) -- true 10 end
print("main", coroutine.resume(co, "x", "y")) -- cannot resume dead coroutine
