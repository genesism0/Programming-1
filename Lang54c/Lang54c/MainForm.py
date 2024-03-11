import System.Drawing
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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Plum
		self._button1.Font = System.Drawing.Font("Poor Richard", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(255, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(136, 53)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Plum
		self._button2.Font = System.Drawing.Font("Poor Richard", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(253, 92)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(138, 57)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Plum
		self._button3.Font = System.Drawing.Font("Poor Richard", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(255, 185)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(136, 56)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Indigo
		self._label1.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Thistle
		self._label1.Location = System.Drawing.Point(8, 113)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(126, 36)
		self._label1.TabIndex = 7
		self._label1.Text = "Radius:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Indigo
		self._label2.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Thistle
		self._label2.Location = System.Drawing.Point(8, 158)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(126, 35)
		self._label2.TabIndex = 8
		self._label2.Text = "Area:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Indigo
		self._label3.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Thistle
		self._label3.Location = System.Drawing.Point(8, 205)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(126, 36)
		self._label3.TabIndex = 9
		self._label3.Text = "Circumference:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Thistle
		self._label4.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Indigo
		self._label4.Location = System.Drawing.Point(140, 113)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(107, 36)
		self._label4.TabIndex = 10
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Thistle
		self._label5.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Indigo
		self._label5.Location = System.Drawing.Point(140, 158)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(107, 35)
		self._label5.TabIndex = 11
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Thistle
		self._label6.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Indigo
		self._label6.Location = System.Drawing.Point(140, 205)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(107, 36)
		self._label6.TabIndex = 12
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(76, 45)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(121, 20)
		self._textBox1.TabIndex = 13
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(401, 257)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54c"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		num1 = int(self._textBox1)
		pi = 3.14159
		Circumference = 2
		area = pi * radius**2)
		pass