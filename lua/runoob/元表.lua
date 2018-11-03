-- 在 Lua table 中我们可以访问对应的key来得到value值，但是却无法对两个 table 进行操作。
-- 因此 Lua 提供了元表(Metatable)，允许我们改变table的行为，每个行为关联了对应的元方法。
-- 例如，使用元表我们可以定义Lua如何计算两个table的相加操作a+b。
-- 元表:C++虚表

other = { foo = 3 } 
t = setmetatable({}, { __index = other }) 
print(t.foo)
print(t.bar)

mytable = setmetatable({key1 = "value1"}, {
  __index = function(mytable, key)
    if key == "key2" then
      return "metatablevalue"
    else
      return nil
    end
  end
})

print(mytable.key1,mytable.key2)

mymetatable = {}
mytable = setmetatable({key1 = "value1"}, { __newindex = mymetatable })

print(mytable.key1)

mytable.newkey = "新值2"
print(mytable.newkey,mymetatable.newkey)

mytable.key1 = "新值1"
print(mytable.key1,mymetatable.key1)

mytable = setmetatable({key1 = "value1"}, {
  __newindex = function(mytable, key, value)
        rawset(mytable, key, "\""..value.."\"")

  end
})

mytable.key1 = "new value"
mytable.key2 = 4

print(mytable.key1,mytable.key2)

-- 计算表中最大值，table.maxn在Lua5.2以上版本中已无法使用
-- 自定义计算表中最大键值函数 table_maxn，即计算表的元素个数
function table_maxn(t)
    local mn = 0
    for k, v in pairs(t) do
        if mn < k then
            mn = k
        end
    end
    return mn
end

-- 两表相加操作
mytable = setmetatable({ 1, 2, 3 }, {
  __add = function(mytable, newtable)
    for i = 1, table_maxn(newtable) do
      table.insert(mytable, table_maxn(mytable)+1,newtable[i])
    end
    return mytable
  end
})

secondtable = {4,5,6}

mytable = mytable + secondtable
    for k,v in ipairs(mytable) do
print(k,v)
end