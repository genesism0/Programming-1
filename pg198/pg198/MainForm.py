import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Location = System.Drawing.Point(15, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(221, 172)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Tickets Sold"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label12)
		self._groupBox2.Controls.Add(self._label11)
		self._groupBox2.Controls.Add(self._label10)
		self._groupBox2.Controls.Add(self._label9)
		self._groupBox2.Controls.Add(self._label8)
		self._groupBox2.Controls.Add(self._label5)
		self._groupBox2.Controls.Add(self._label6)
		self._groupBox2.Controls.Add(self._label7)
		self._groupBox2.Location = System.Drawing.Point(253, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(221, 172)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Revenue Generated"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.PaleTurquoise
		self._label1.Location = System.Drawing.Point(21, 14)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(173, 30)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of tickets sold for each class of seats"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumAquamarine
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(21, 63)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(59, 17)
		self._label2.TabIndex = 1
		self._label2.Text = "Class A:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumAquamarine
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(21, 98)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(59, 17)
		self._label3.TabIndex = 2
		self._label3.Text = "Class B:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MediumAquamarine
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(21, 133)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(59, 16)
		self._label4.TabIndex = 3
		self._label4.Text = "Class C:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.MediumAquamarine
		self._label5.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(52, 26)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(57, 18)
		self._label5.TabIndex = 4
		self._label5.Text = "Class A:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.MediumAquamarine
		self._label6.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(52, 60)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(57, 18)
		self._label6.TabIndex = 5
		self._label6.Text = "Class B:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.MediumAquamarine
		self._label7.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(51, 98)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(58, 17)
		self._label7.TabIndex = 6
		self._label7.Text = "Class C:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label8.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(6, 133)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(103, 19)
		self._label8.TabIndex = 7
		self._label8.Text = "Total Revenue:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(100, 63)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(94, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(100, 95)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(94, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(100, 133)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(94, 20)
		self._textBox3.TabIndex = 6
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label9.Location = System.Drawing.Point(115, 26)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 18)
		self._label9.TabIndex = 8
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label10.Location = System.Drawing.Point(115, 63)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 18)
		self._label10.TabIndex = 9
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label11.Location = System.Drawing.Point(115, 101)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 18)
		self._label11.TabIndex = 10
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label12.Location = System.Drawing.Point(115, 136)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 18)
		self._label12.TabIndex = 9
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Transparent
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(43, 190)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(149, 38)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate Revenue"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Transparent
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(205, 190)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 38)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Transparent
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(333, 190)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(110, 38)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(484, 234)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg198"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		A = int(self._textBox1.Text)
		B = int(self._textBox2.Text)
		C = int(self._textBox3.Text)
		classA = A * 15
		classB = B * 12
		classC = C * 9
		totalRev = classA + classB + classC
		self._label9.Text = str(classA)
		self._label10.Text = str(classB)
		self._label11.Text = str(classC)
		self._label12.Text = str(totalRev)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		
	def Button3Click(self, sender, e):
		Application.Exit()