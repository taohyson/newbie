local newProducer

function produce( ... )
	local i = 0
	while true do
		coroutine.yield(i)
		i = i + 1
	end
end

function comsume( ... )
	while true do
		local status, value = coroutine.resume(newProducer)
		print(value)
	end
end

newProducer = coroutine.create(produce)
comsume()