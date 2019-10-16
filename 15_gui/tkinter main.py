#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
 tkinter 相关
"""

from tkinter import *
from tkinter import Frame
import tkinter.messagebox as messagebox


# class Application(Frame):
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createwidgets()
#
#     def createwidgets(self):
#         self.helloLabel = Label(self, text='Hello, world! ')
#         self.helloLabel.pack()
#
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createwidgets()

    def createwidgets(self):

        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.quitButton = Button(self, text='Hello', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()

# 设置窗口标题
app.master.title('Hello World')

# 主消息循环
app.mainloop()








