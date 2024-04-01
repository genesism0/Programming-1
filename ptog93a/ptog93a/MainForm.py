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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(7, 205)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(78, 51)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(91, 205)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 51)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(172, 205)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(79, 51)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Kilowatts used:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(151, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 53)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(133, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Base Rate:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(151, 53)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(9, 99)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(112, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Citytax:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(142, 99)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(9, 137)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Pay this amount:"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(155, 137)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 10
		self._label7.Text = "label7"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(7, 171)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 11
		self._label8.Text = "After May 20th Pay:"
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(142, 171)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 12
		self._label9.Text = "label9"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(267, 258)
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
		Kilowatts = int(self._textBox.Text)
		Kilowatts*4.75

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()