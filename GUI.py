# GUI.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton1 = Button(self, text = 'Hello', command = self.hello)
		self.alertButton2 = Button(self, text = 'Fuck', command = self.hello)
		self.alertButton1.pack()
		self.alertButton2.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		tkMessageBox.showinfo('Message', 'Hello, %s' % name)
		

app = Application()
app.master.title('test by wyn')
app.mainloop()