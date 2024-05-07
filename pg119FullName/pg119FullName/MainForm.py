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
		self._label1.BackColor = System.Drawing.Color.SeaGreen
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(7, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(159, 27)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter your First name:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SeaGreen
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(7, 76)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(159, 27)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter your Last name:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SeaGreen
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(7, 140)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(159, 27)
		self._label3.TabIndex = 2
		self._label3.Text = "This is your full name:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(172, 140)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(127, 27)
		self._label4.TabIndex = 3
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.ForestGreen
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(172, 9)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(127, 27)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.ForestGreen
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(170, 76)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(129, 27)
		self._textBox2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumSeaGreen
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(7, 183)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(92, 28)
		self._button1.TabIndex = 6
		self._button1.Text = "Show Name"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumSeaGreen
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(109, 183)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(92, 28)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MediumSeaGreen
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(207, 183)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(92, 28)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightCyan
		self.ClientSize = System.Drawing.Size(316, 221)
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
		self.Text = "pg119FullName"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		strFullName = ""
		strFullName = self._txtFirstName.Text + " " + self._txtLastName.Text
		self._lblFullName = strFullName
		#first = self._textbox1.Text
		#last = self._textBox2.Text
		#full = first + last
		#self._label1.Text = str(full)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()