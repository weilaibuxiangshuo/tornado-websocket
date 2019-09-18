import time
import threading

gen=None

def IongIo():
    def run():
        print("开始AA")
        time.sleep(3)
        print("结束AA")
        try:
            # 返回数据
            global gen
            gen.send('这个是返回数据')
        except StopIteration as e:
            pass
    threading.Thread(target=run).start()

# def genCoroutine(func):
#     def wrapper(*args,**kwargs):
#         gen1=func()
#         gen2=next(gen1)
#         def run(g):
#             res = next(g)
#             try:
#                 gen1.send(res) #返回给B数据
#             except StopIteration as e:
#                 pass
#         threading.Thread(target=run,args=(gen2,)).start()
#     return wrapper
#
#
# @genCoroutine
# def B():
#     print("开始B")
#     res= yield IongIo()
#     print("接收到的数据",res)
#     print("结束B")



# def IongIo(callback):
#     def wrapper(func):
#         print("开始AA")
#         time.sleep(3)
#         print("结束AA")
#         data="这个是处理完要返回的结果"
#         func(data)
#     threading.Thread(target=wrapper,args=(callback,)).start()
#
#
# def finish(data):
#     print("开始处理回调数据")
#     print("正在处理回调数据",data)
#     print("结束处理回调数据")
#
#


def gencontent(func):
    def wrapper():
        global gen
        gen = func()
        next(gen)
    return wrapper

@gencontent
def B():
    print("开始B")
    res= yield IongIo()
    print("接收到的数据",res)
    print("结束B")


def C():
    print("开始C")
    print("结束C")

def main():
    B()
    C()

if __name__=="__main__":
    main()

