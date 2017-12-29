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
		self.alertButton2 = Button(self, text = 'Fuck1', command = self.hello)
		self.alertButton3 = Button(self, text = 'Fuck2', command = self.hello)
		self.alertButton4 = Button(self, text = 'Fuck3', command = self.hello)
		self.alertButton5 = Button(self, text = 'Fuck4', command = self.hello)
		self.alertButton6 = Button(self, text = 'Fuck5', command = self.hello)
		self.alertButton7 = Button(self, text = 'Fuck6', command = self.hello)
		self.alertButton1.pack()
		self.alertButton2.pack()
		self.alertButton3.pack()
		self.alertButton4.pack()
		self.alertButton5.pack()
		self.alertButton6.pack()
		self.alertButton7.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		tkMessageBox.showinfo('Message', 'Hello, %s' % name)
		

app = Application()
app.master.title('test by wyn')
app.mainloop()