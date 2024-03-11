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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(164, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(189, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Import Math"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 72)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(19, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "A:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(153, 69)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(18, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "B:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(312, 69)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(30, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "C:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(28, 69)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(193, 69)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(333, 66)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 272)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(158, 46)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(243, 272)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(130, 46)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(358, 295)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(495, 372)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang58b"
		self.ResumeLayout(False)
		self.PerformLayout()

