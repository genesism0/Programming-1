﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LavenderBlush
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(228, 6)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(136, 57)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.HotPink
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(228, 73)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(136, 55)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Plum
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(228, 139)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(136, 55)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.Location = System.Drawing.Point(7, 6)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Kilowatts used:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(118, 6)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(104, 23)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Pink
		self._label2.Location = System.Drawing.Point(7, 40)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Base Rate:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.PaleVioletRed
		self._label3.Location = System.Drawing.Point(118, 40)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Location = System.Drawing.Point(7, 73)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Surcharge:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.PaleVioletRed
		self._label5.Location = System.Drawing.Point(118, 73)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Pink
		self._label6.Location = System.Drawing.Point(7, 105)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Citytax:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.PaleVioletRed
		self._label7.Location = System.Drawing.Point(118, 105)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 10
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Pink
		self._label8.Location = System.Drawing.Point(7, 137)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 11
		self._label8.Text = "Pay this amount:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.PaleVioletRed
		self._label9.Location = System.Drawing.Point(118, 137)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 12
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Pink
		self._label10.Location = System.Drawing.Point(7, 171)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 13
		self._label10.Text = "After May 20th Pay:"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.PaleVioletRed
		self._label11.Location = System.Drawing.Point(118, 171)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Thistle
		self.ClientSize = System.Drawing.Size(376, 206)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "ptog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Kilowatts = int(self._textBox1.Text)
		baseR = Kilowatts  * 0.0475
		baseR = round(baseR, 2)
		surcharge = baseR * 0.1
		surcharge = round(surcharge, 2)
		cityT = baseR * 0.03
		cityT = round(cityT, 2)
		total = baseR + surcharge + cityT
		lateF = total + total * 0.04
		lateF = round(lateF, 2)
		
		self._label3.Text = str(baseR)
		self._label5.Text = str(surcharge)
		self._label7.Text = str(cityT)
		self._label9.Text = str(total)
		self._label11.Text = str(lateF)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label3.Text = ""
		self._label5.Text = ""
		self._label7.Text = ""
		self._label9.Text = ""
		self._label11.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()