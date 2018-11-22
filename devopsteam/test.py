# -*- coding: utf-8 -*-
from multiprocessing import Process
import time
from tkinter import *
from tkinter.messagebox import askyesno
import psutil
from testmy import TestMy
from job import Job
from queue import Queue
import threading
import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='system.log',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


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


class ProgressBar():
    def __init__(self, root):
        self.root = root

    def closeWindow(self):
        ans = askyesno(title='Warning', message='Close the window?')
        if ans:
            root.destroy()
        else:
            return

    def info(self):
        # print(title)
        print('module name:', __name__)
        print('parent process:', os.getppid())
        print('process id:', os.getpid())
        b = Button(self.root, textvariable=v, command=self.changeText)
        gb = Button(self.root, textvariable=g, command=self.closeEnd)
        g.set('Close')
        v.set('Start')
        b.pack()
        gb.pack()
        self.root.protocol('WM_DELETE_WINDOW', self.closeWindow)
        self.root.mainloop()

    def changeText(self):
        print('a')
        runp = Process(target=starssss.main(), args=())
        runp.start()

    def closeEnd(self):
        print('b')

    def f(self, name):
        logging.info('function f')
        print('hello', name)

    def mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    logging.info('main line')
    root = Tk()
    v = StringVar()
    g = StringVar()
    starssss = TestMy()
    PB = ProgressBar(root)
    pr1 = Process(target=PB.info(), args=())
    pr1.start()


