﻿import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.PaleVioletRed
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(151, 24)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.PaleVioletRed
		self._label2.Location = System.Drawing.Point(12, 52)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(151, 24)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay periods per year"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.PaleVioletRed
		self._label3.Location = System.Drawing.Point(12, 90)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(151, 24)
		self._label3.TabIndex = 2
		self._label3.Text = "Salary per pay period:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Location = System.Drawing.Point(179, 90)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(151, 24)
		self._label4.TabIndex = 3
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(179, 52)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(151, 24)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(179, 13)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(151, 24)
		self._textBox2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(14, 127)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 34)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(118, 127)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 34)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(222, 127)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 34)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(343, 173)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.RightToLeftLayout = True
		self.Text = "pg153"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		S = float(self._textBox1.Text)
		P = int(self._textBox2.Text)
		decsalary = S // P
		self._label4.Text = str(decsalary)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()