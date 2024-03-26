import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from math import sqrt

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(234, 59)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(128, 39)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(234, 147)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(128, 39)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._button3.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(234, 104)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(128, 37)
		self._button3.TabIndex = 2
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.SeaGreen
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(12, 6)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(109, 34)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.SeaGreen
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(127, 6)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(117, 34)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.SeaGreen
		self._textBox3.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(250, 6)
		self._textBox3.Multiline = True
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(112, 34)
		self._textBox3.TabIndex = 5
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label1.Location = System.Drawing.Point(17, 74)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(75, 32)
		self._label1.TabIndex = 6
		self._label1.Text = "Root:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumSeaGreen
		self._label2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(98, 74)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(109, 32)
		self._label2.TabIndex = 7
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label3.Location = System.Drawing.Point(17, 125)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(75, 30)
		self._label3.TabIndex = 8
		self._label3.Text = "Root:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MediumSeaGreen
		self._label4.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(98, 125)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(109, 30)
		self._label4.TabIndex = 9
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(374, 198)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog58b"
		
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		A = int(self._textBox1.Text)
		B = int(self._textBox2.Text)
		C = int(self._textBox3.Text)
		Root1 = (-B + math.sqrt(B**2 - 4 * A * C))/2*A
		Root2 = (-B - math.sqrt(B**2 - 4 * A * C))/2*A
		self._label2.Text = str(Root1)
		self._label4.Text = str(Root2)
		

	def Button3Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label2.Text = ""
		self._label4.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()