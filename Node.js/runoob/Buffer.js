// Buffer 与字符编码
const buf = Buffer.from('runoob', 'ascii');
console.log(buf.toString('hex'));
console.log(buf.toString('base64'));

// 创建 Buffer 类
buf1 = Buffer.alloc(10);
buf2 = Buffer.alloc(10,1);
buf3 = Buffer.allocUnsafe(10);
buf4 = Buffer.from([1,2,3]);
buf5 = Buffer.from('test');
buf6 = Buffer.from('test', 'latin1');

// 写入缓冲区
buf7 = Buffer.alloc(256);
len = buf7.write('www.runoob.com');
console.log(buf7.toString());
console.log(len);

// 从缓冲区读取数据
buf8 = Buffer.alloc(26);
for (var i = buf8.length - 1; i >= 0; i--) {
	buf8[i] = i + 97;
}
console.log(buf8.toString('ascii',0,21));

// 将 Buffer 转换为 JSON 对象
const buf9 = Buffer.from([1,2,3,4,5]);
json = JSON.stringify(buf9);
console.log(json);
const copy = JSON.parse(json, (key,value) => {
	return value && value.type == 'Buffer' ? Buffer.from(value) : value;
});
console.log(copy);

// 缓冲区合并
var buffer1 = Buffer.from(('菜鸟教程'));
var buffer2 = Buffer.from(('www.runoob.com'));
var buffer3 = Buffer.concat([buffer1,buffer2]);
console.log("buffer3 内容: " + buffer3.toString());	

// 缓冲区比较
var buffer1 = Buffer.from('ABC');
var buffer2 = Buffer.from('ABCD');
var result = buffer1.compare(buffer2);
if(result < 0) {
   console.log(buffer1 + " 在 " + buffer2 + "之前");
}else if(result == 0){
   console.log(buffer1 + " 与 " + buffer2 + "相同");
}else {
   console.log(buffer1 + " 在 " + buffer2 + "之后");
}

// 拷贝缓冲区
var buf1 = Buffer.from('abcdefghijkl');
var buf2 = Buffer.from('RUNOOB');
buf2.copy(buf1, 2);
console.log(buf1.toString());

// 缓冲区裁剪
var buffer1 = Buffer.from('runoob');
var buffer2 = buffer1.slice(0,2);
console.log("buffer2 content: " + buffer2.toString());

// 缓冲区长度
var buffer = Buffer.from('www.runoob.com');
console.log("buffer length: " + buffer.length);