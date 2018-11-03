string1 = "Lua"
print("\"字符串 1 是\"",string1)
string2 = 'runoob.com'
print("字符串 2 是",string2)

string3 = [["Lua 教程"]]
print("字符串 3 是",string3)

string1 = "Lua";
print(string.upper(string1))
print(string.lower(string1))

string = "Lua Tutorial"
-- 查找字符串
print(string.find(string,"Tutorial"))
reversedString = string.reverse(string)
print("新字符串为",reversedString)

string1 = "Lua"
string2 = "Tutorial"
number1 = 10
number2 = 20
-- 基本字符串格式化
print(string.format("基本格式化 %s %s",string1,string2))
-- 日期格式化
date = 2; month = 1; year = 2014
print(string.format("日期格式化 %02d/%02d/%03d", date, month, year))
-- 十进制格式化
print(string.format("%.4f",1/3))
string.format("%c", 83)
string.format("%+d", 17.0)
string.format("%05d", 17)
string.format("%o", 17)
string.format("%u", 3.14)
string.format("%x", 13)
string.format("%X", 13)
string.format("%e", 1000)
string.format("%E", 1000)
string.format("%6.3f", 13)
string.format("%q", "One\nTwo")
string.format("%s", "monkey")
string.format("%10s", "monkey")
string.format("%5.3s", "monkey")

-- 字符转换
-- 转换第一个字符
print(string.byte("Lua"))
-- 转换第三个字符
print(string.byte("Lua",3))
-- 转换末尾第一个字符
print(string.byte("Lua",-1))
-- 第二个字符
print(string.byte("Lua",2))
-- 转换末尾第二个字符
print(string.byte("Lua",-2))

-- 整数 ASCII 码转换为字符
print(string.char(97))

string1 = "www."
string2 = "runoob"
string3 = ".com"
-- 使用 .. 进行字符串连接
print("连接字符串",string1..string2..string3)

-- 字符串长度
print("字符串长度 ",string.len(string2))

-- 字符串复制 2 次
repeatedString = string.rep(string2,2)
print(repeatedString)

s = "Deadline is 30/05/1999, firm"
date = "%d%d/%d%d/%d%d%d%d"
print(string.gsub(s, string.find(s, date)))    --> 30/05/1999