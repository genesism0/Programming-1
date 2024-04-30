import System.Drawing
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
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Lavender
		self._listBox1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 17
		self._listBox1.Location = System.Drawing.Point(5, 32)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(212, 174)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Pink
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(5, 212)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(212, 42)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleVioletRed
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(5, 257)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(212, 42)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.HotPink
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(5, 303)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(212, 42)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Plum
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(5, 4)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(87, 25)
		self._label1.TabIndex = 4
		self._label1.Text = "Test Value:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(98, 4)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(119, 25)
		self._textBox1.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SlateBlue
		self.ClientSize = System.Drawing.Size(222, 352)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()




	def Button1Click(self, sender, e):
		num = self._textBox1.Text()
		heading = "Even Interger" + "\t\t" + "Sum"
		self._listBox1.Items.Add(heading)
		
		

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		pass