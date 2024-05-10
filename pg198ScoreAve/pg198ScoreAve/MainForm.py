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
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(67, 20)
		self._label1.TabIndex = 0
		self._label1.Text = "Score 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 63)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(67, 20)
		self._label2.TabIndex = 1
		self._label2.Text = "Score 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(6, 93)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(67, 17)
		self._label3.TabIndex = 2
		self._label3.Text = "Score 3:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.OliveDrab
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(6, 123)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(67, 23)
		self._label4.TabIndex = 1
		self._label4.Text = "Average:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(88, 27)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 21)
		self._textBox1.TabIndex = 3
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(203, 163)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Enter Three Test Scores"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(88, 63)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(88, 94)
		self._textBox3.Multiline = True
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 21)
		self._textBox3.TabIndex = 5
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DarkOliveGreen
		self._label5.Location = System.Drawing.Point(88, 123)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "label5"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 193)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(85, 46)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate Average"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(109, 181)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(106, 32)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(109, 216)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(106, 32)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(231, 267)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg198ScoreAve"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		Score1 = int(self._textBox1.Text)
		Score2 = int(self._textBox2.Text)
		Score3 = int(self._textBox3.Text)
		ave = Score1 + Score2 + Score3
		ave = ave / 3
		self._label5.Text = str(ave)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""
		

	def Button3Click(self, sender, e):
		Application.Exit()