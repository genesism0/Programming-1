﻿import System.Drawing
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
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumTurquoise
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumTurquoise
		self._label2.Location = System.Drawing.Point(12, 71)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Operation:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumTurquoise
		self._label3.Location = System.Drawing.Point(12, 132)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Number 2:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MediumTurquoise
		self._label4.Location = System.Drawing.Point(12, 180)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Result:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SkyBlue
		self._label5.Location = System.Drawing.Point(132, 71)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightCyan
		self._textBox1.Location = System.Drawing.Point(132, 9)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 23)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightCyan
		self._textBox2.Location = System.Drawing.Point(132, 132)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 23)
		self._textBox2.TabIndex = 6
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label6.Location = System.Drawing.Point(132, 180)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(248, 8)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(38, 34)
		self._button1.TabIndex = 8
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(292, 8)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(36, 34)
		self._button2.TabIndex = 9
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(334, 9)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(36, 34)
		self._button3.TabIndex = 10
		self._button3.Text = "*"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(248, 46)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(35, 34)
		self._button4.TabIndex = 11
		self._button4.Text = "^"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(292, 48)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(36, 34)
		self._button5.TabIndex = 12
		self._button5.Text = "/"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(335, 49)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(35, 33)
		self._button6.TabIndex = 13
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(282, 86)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(58, 23)
		self._button7.TabIndex = 14
		self._button7.Text = "MOD"
		self._button7.UseVisualStyleBackColor = True
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(248, 121)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(122, 35)
		self._button8.TabIndex = 15
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Location = System.Drawing.Point(248, 168)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(122, 35)
		self._button9.TabIndex = 16
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(378, 217)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg140"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "+"
		sum = num1 + num2
		self._label6.Text = str(sum)

	def Button2Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "-"
		out = num1 - num2
		self._label6.Text = str(out)
		
	def Button3Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "*"
		mul = num1 * num2
		self._label6.Text = str(mul)
		
	def Button4Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "^"
		pr = num1 ** num2
		self._label6.Text = str(pr)

	def Button5Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "/"
		div = num1 / num2
		self._label6.Text = str(div)
		
	def Button6Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "//"
		divs = num1 // num2
		self._label6.Text = str(divs)

	def Button8Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button9Click(self, sender, e):
		Application.Exit()