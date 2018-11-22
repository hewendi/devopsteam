# -*- coding: utf-8 -*-
import multiprocessing
from multiprocessing import Process, current_process
import time
from tkinter import *
from tkinter.filedialog import askopenfilename,askdirectory
import tkinter.messagebox as messagebox
from tkinter.messagebox import askyesno
# from queue import Queue
import psutil
import os
import logging
from selenium import webdriver
logging.basicConfig(level=logging.DEBUG,
                    filename='system.log',
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )


class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        self.procepid = None

    def run(self):
        browser = webdriver.Chrome()
        time.sleep(5)
        url = "http://www.baidu.com"
        browser.get(url)
        time.sleep(5)
        browser.find_element_by_id("kw").send_keys("python")
        time.sleep(5)
        browser.find_element_by_id("su").click()
        time.sleep(5)
        browser.close()


class TestMy():
    def __int__(self):
        self.aa=2

    def adf(self):
        browser = webdriver.Chrome()
        time.sleep(5)
        url = "http://www.baidu.com"
        browser.get(url)
        time.sleep(5)
        browser.find_element_by_id("kw").send_keys("python")
        time.sleep(5)
        browser.find_element_by_id("su").click()
        time.sleep(5)
        browser.close()
        # btnv.set('Start')

    def mains(self,):
        # print(v.get())
        self.adf()




class ProgressBar():
    def __init__(self, master):
        self.root = master
        self.parent_pid = os.getppid()
        self.sub_pid = None
        self.sub_sub_pid = None

    def closeWindow(self):
        ans = askyesno(title='Warning', message='Close the window?')
        if ans:
            if self.sub_pid is not None:
                Cpro = psutil.Process(self.sub_pid)
                Cpro.kill()

            self.root.destroy()
        else:
            return

    def changeText(self):
        print('a')
        # broswer
        sub_proc2 = MyProcess()
        self.sub_pid = sub_proc2.pid
        sub_proc2.start()

    def closeEnd(self):
        print('b')

    def fqqqq(self):
        logging.info('function f')
        starssss = TestMy()
        starssss.mains()

    def mainloop(self):
        self.root.mainloop()


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    logging.info('main2')
    root = Tk()
    v = StringVar()
    g = StringVar()

    ps = ProgressBar(root)
    b = Button(root, textvariable=v, command=ps.changeText)
    gb = Button(root, textvariable=g, command=ps.closeEnd)
    v.set('Start')
    g.set('Close')
    b.pack()
    gb.pack()
    root.protocol('WM_DELETE_WINDOW', ps.closeWindow)
    print('mian lind end')
    root.mainloop()
    print('mian lind end2')
    logging.info('main3')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    logging.info('main1')
    run_proc('name')
#
#
# # if __name__ == '__main__':
# # print('Parent process %s.' % os.getpid())
# # p = Process(target=run_proc, args=('test',))
# # p.start()
# # p.join()
# # print('End')

