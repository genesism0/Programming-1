﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(34, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(243, 134)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 173)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(109, 173)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(83, 25)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(202, 174)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(322, 252)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number" + "\t" "Square" + "\t" "Square Root" + "\t" "Cube" + "\t" "4th Root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 20+1):
			square = num*num
			sq = 

	def Button2Click(self, sender, e):
		self.listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()