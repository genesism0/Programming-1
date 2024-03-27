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
		self._listBox1.Location = System.Drawing.Point(6, 5)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(306, 186)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PowderBlue
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(6, 208)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(106, 38)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightBlue
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(118, 208)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(96, 38)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SteelBlue
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(220, 208)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(92, 38)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CadetBlue
		self.ClientSize = System.Drawing.Size(318, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog162b"
		self.ResumeLayout(False)



	def Button1Click(self, sender, e):
		heading = "Year\t\tPopulation (in mil.)"
		self._listBox1.Items.Clear(heading)
		pop = 243 # 1990
		for year in range(1991, 2016):
			line = str(year) + "\t\t" + str(int(pop))
			self._listBox1.Items.Add(line)
			pop *= 1.029 # pop = pop * 1.029

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()