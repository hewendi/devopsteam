# -*- coding: utf-8 -*-
from multiprocessing import Process
import time
from tkinter import *
import psutil
from testmy import TestMy
from job import Job
from queue import Queue
import threading

class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        self.procepid = None
        # self.master = master
        # self.queue = Queue()

    def run(self):
        starssss = TestMy()
        starssss.adf()
        # for i in range(1000):
        #     time.sleep(2)
        #     print('hello ' + str(i), self.name, time.ctime())


def changeText():
    if v.get() == 'Start':
        starssss = TestMy()
        tt = threading.Thread(target=starssss.main, args=(event_obj, v))
        tt.start()
        # event_obj.set()
        v.set('pause')
        print('start')
    elif v.get() == 'pause':
        event_obj.clear()
        v.set('resume')
        print('pause')
    else:
        event_obj.set()
        v.set('pause')
        print('resume')


def closeEnd():
    aaa = 1


root = Tk()
v = StringVar()
g = StringVar()

# tt = Job()
event_obj = threading.Event()  # 创建一个事件
event_obj.clear()


b = Button(root, textvariable=v, command=changeText)
gb = Button(root, textvariable=g, command=closeEnd)
g.set('Close')
v.set('Start')
b.pack()
gb.pack()
root.mainloop()
