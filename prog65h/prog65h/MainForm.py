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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Green
		self._button1.Font = System.Drawing.Font("Modern No. 20", 23.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(255, 9)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(139, 56)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Green
		self._button2.Font = System.Drawing.Font("Modern No. 20", 23.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(255, 83)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(139, 56)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Green
		self._button3.Font = System.Drawing.Font("Modern No. 20", 23.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(260, 145)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(138, 56)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(137, 13)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 32)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(139, 60)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(98, 32)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(137, 117)
		self._textBox3.Multiline = True
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 32)
		self._textBox3.TabIndex = 5
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightGreen
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(119, 32)
		self._label1.TabIndex = 6
		self._label1.Text = "Enter Pounds:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightGreen
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(12, 60)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(119, 32)
		self._label2.TabIndex = 7
		self._label2.Text = "Enter Shillings:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightGreen
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(12, 117)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(119, 32)
		self._label3.TabIndex = 8
		self._label3.Text = "Enter Pence:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightGreen
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(12, 169)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(119, 32)
		self._label4.TabIndex = 9
		self._label4.Text = "Decimal Pounds:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label5.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(137, 169)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 32)
		self._label5.TabIndex = 10
		self._label5.Text = "label5"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Ivory
		self.ClientSize = System.Drawing.Size(406, 212)
		self.Controls.Add(self._label5)
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
		self.Text = "prog65h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pounds = int(self.textBox1.Text)
		shillings = int(self.textBox2.Text)
		pence = int(self.textBox2.Text)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""