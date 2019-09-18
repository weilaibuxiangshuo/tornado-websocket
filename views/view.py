from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient
import time,json
import tornado.web
from tornado.websocket import WebSocketHandler

class Indexhandler(RequestHandler):
    def get(self):
        self.render('index.html')

#回调异步
class Homehandler(RequestHandler):
    def on_response(self,response):
        print('asdfasdfsadf')
        if response.error:
            print('error',response.error)
            self.send_error(500)
        else:
            data = json.loads(response.body)
            # print(response.body,'body')
            self.write(data)
        self.finish()

    def ceshi(self):
        print("你好")

    @tornado.web.asynchronous    #不关闭长连接
    def get(self, *args, **kwargs):
        url = 'https://www.layui.com/demo/table/user/'

        # 创建客户端
        client = AsyncHTTPClient()
        client.fetch(url, self.on_response)
        self.write("home")

#协程异步
class Studentshandler(RequestHandler):
    @tornado.gen.coroutine      #协程装饰器
    def get(self,*args,**kwargs):
        url = 'https://www.layui.com/demo/table/user/'
        # 创建客户端
        client = AsyncHTTPClient()
        res=yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(data)


class Students2handler(RequestHandler):
    @tornado.gen.coroutine   #协程装饰器
    def get(self,*args,**kwargs):
        res = yield self.getData()
        self.write(res)

    @tornado.gen.coroutine
    def getData(self):
        url = 'https://www.layui.com/demo/table/user/'
        # 创建客户端
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            ret={"ret":0}
        else:
            ret = json.loads(res.body)
        raise tornado.gen.Return(ret)


class Worldhandler(WebSocketHandler):
    def get(self):
        self.render('chat.html')


class Chathandler(WebSocketHandler):
    users=[]
    """websocket建立连接后调用"""
    def open(self):
        print('chat')
        self.users.append(self)
        print(self.users)
        for user in self.users:
            """
            write_message可以主动向客户端发送消息
            可以是字符串或者字典，字典自动转为json字符串
            参数：
            binary为false,则message会以utf-8编码发送
            inary为True,则message会以二进制编码发送，即字节码
            """
            print(self.request.remote_ip)
            user.write_message("%s登陆了"%(self.request.remote_ip))

    """当客户端发送消息后调用"""
    def on_message(self, message):
        print(message,'message')
        for user in self.users:
            print(user)
            user.write_message("%s说:%s"%(self.request.remote_ip,message))


    """websocket连接关闭后调用"""
    def on_close(self):
        """删除自己"""
        self.users.remove(self)
        for user in self.users:
            print(self.request.remote_ip)
            user.write_message("%s退出了"%(self.request.remote_ip))


    """判断源origin，请于符合条件的请求允许连接"""
    def check_origin(self, origin):
        return True
