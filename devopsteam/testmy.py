# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import time
import threading


class BackendProcess:
    def __init__(self):
        self.finished = False

    def task(self):
        time.sleep(2)
        print('finished')
        self.finished = True

    def run(self):
        thread = threading.Thread(target=self.task, daemon=True)
        thread.start()


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.process = BackendProcess()
        qq = tk.Button(self, text='Run', command=self.run)
        # qq.bind('<Control-Key-1>', self.check_process2)
        qq.pack(expand='yes')

    def run(self):
        self.process.run()
        self.check_process()

    def check_process(self):
        """ Check every 1000 ms whether the process is finished """
        if self.process.finished:
            messagebox.showinfo('Info', 'Process completed')
        else:
            self.after(1000, self.check_process)

    def check_process2(self, event=None):
        """ Check every 1000 ms whether the process is finished """
        messagebox.showinfo('Info', 'Process completed')


if __name__ == '__main__':
    gui = GUI()
    gui.bind('<Control-Shift-Key-P>', gui.check_process2)
    gui.mainloop()

















# import tkinter
import time
# import threading
# import random
# from queue import Queue



# class GuiPart():
#     def __init__(self, master, queue, start_command, stop_command, continue_command, kill_command):
#         self.queue = queue
#         tkinter.Button(master, text='Start', command=start_command).pack()
#         tkinter.Button(master, text='Stop', command=stop_command).pack()
#         tkinter.Button(master, text='Continue', command=continue_command).pack()
#         tkinter.Button(master, text='Kill', command=kill_command).pack()
#
#     def processIncoming(self):
#         while self.queue.qsize():
#             try:
#                 msg = self.queue.get(0)
#                 print(msg)
#             except Queue.Empty:
#                 pass
#
#
# class ThreadedClient():
#     def __init__(self, master):
#         self.master = master
#         self.queue = Queue()
#         self.gui = GuiPart(master, self.queue, self.web_driver, self.web_stop, self.web_continum, self.web_kill)
#         self.running = True
#         self.thread1 = threading.Thread(target=self.workerThread1)
#         self.thread1.start()
#         self.periodicCall()
#
#     def periodicCall(self):
#         self.master.after(200, self.periodicCall)
#         self.gui.processIncoming()
#         if not self.running:
#             self.master.destroy()
#
#     def workerThread1(self):
#         # self.ott=Tkinter.Tk()
#         # self.ott.mainloop()
#         while self.running:
#             time.sleep(rand.random() * 1.5)
#             msg = rand.random()
#             self.queue.put(msg)
#
#     def endApplication(self):
#         self.running = False
#
#     def web_driver(self):
#         browser = webdriver.Ie()
#         url = "http://www.baidu.com"
#         browser.get(url)
#         browser.find_element_by_id("kw").send_keys("python")
#         browser.find_element_by_id("su").click()
#         time.sleep(2)
#         browser.close()
#         self.running = False
#
#     def web_stop(self):
#         pass
#
#     def web_continum(self):
#         pass
#
#     def web_kill(self):
#         pass
#
#
# rand = random.Random()
# root = tkinter.Tk()
# client = ThreadedClient(root)
# root.mainloop()



12
down vote
favorite
8
<Control-Shift-Key-0>
<Control-Key-plus>