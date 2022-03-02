
// define(
//     function (require) {
//         var express= require('express');
//         // const https=require('https');
//         // var request=require('request');

// });

const { request, response } = require('express');
var express = require('express');


//创建应用对象
const app = express();
//创建路由规则
app.get('/server', (request, response) => {
    //设置响应头
    response.setHeader('Access-Control-Allow-Origin', '*');
    // response.setHeader('121.5.48.70','*');
    //若是响应一个数据
    // setTimeout(() => {
    const data = {
        name: "您好，请联系如下电话号码：110"
    }
    //不能直接用send发送，需要转换为字符串格式
    let str = JSON.stringify(data);
    response.send(str);
    // }, 3000)

    // response.send('<html><body</html>');

});

app.get('/submit',(request,response)=>{
    response.setHeader('Access-Control-Allow-Origin', '*');
    response.send("您已提交成功！可以直接登录");
});

app.get('/check-username',(request,response)=>{
    response.setHeader('Access-Control-Allow-Origin', '*');
    const data={
        exist:1,
        msg:"用户名可以"
    };
    let str=JSON.stringify(data);
    response.send(str);

})
//判断客户端传来的用户名是否唯一，若符合保存在本地数据库上
app.get('/success',(request,response)=>{
    // response.sendFile(__dirname+'./success.html')
    response.setHeader('Access-Control-Allow-Origin', '*');
    response.send('您已成功登录！')
})

//监听端口
app.listen(9003, () => {
    console.log("服务器已经启动，端口监听中")
})
