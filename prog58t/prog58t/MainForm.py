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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightPink
		self._label1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(187, 35)
		self._label1.TabIndex = 0
		self._label1.Text = "Purchase Price:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightPink
		self._label2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 53)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(206, 33)
		self._label2.TabIndex = 1
		self._label2.Text = "Amount Recived:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.PaleVioletRed
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(205, 9)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(113, 35)
		self._textBox1.TabIndex = 2
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.PaleVioletRed
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(224, 53)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(113, 35)
		self._textBox2.TabIndex = 3
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(343, 11)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 83)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(343, 116)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 83)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(340, 233)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(132, 83)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightPink
		self._label3.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 97)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(159, 35)
		self._label3.TabIndex = 7
		self._label3.Text = "Change Due:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.PaleVioletRed
		self._label4.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(176, 97)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(113, 35)
		self._label4.TabIndex = 8
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.PaleVioletRed
		self._label5.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(7, 18)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(74, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Dollars:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.PaleVioletRed
		self._label6.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(6, 53)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(84, 23)
		self._label6.TabIndex = 10
		self._label6.Text = "Quarters:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.PaleVioletRed
		self._label7.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(5, 84)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(85, 23)
		self._label7.TabIndex = 11
		self._label7.Text = "Dimes:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.PaleVioletRed
		self._label8.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(5, 115)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(72, 23)
		self._label8.TabIndex = 12
		self._label8.Text = "Nickles:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.PaleVioletRed
		self._label9.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(6, 144)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(75, 23)
		self._label9.TabIndex = 13
		self._label9.Text = "Pennies:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.LightPink
		self._label10.Location = System.Drawing.Point(86, 18)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(99, 23)
		self._label10.TabIndex = 14
		self._label10.Click += self.Label10Click
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.LightPink
		self._label11.Location = System.Drawing.Point(96, 53)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(98, 23)
		self._label11.TabIndex = 15
		self._label11.Click += self.Label11Click
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.LightPink
		self._label12.Location = System.Drawing.Point(96, 84)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 16
		self._label12.Click += self.Label12Click
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.AppWorkspace
		self._groupBox1.Controls.Add(self._label14)
		self._groupBox1.Controls.Add(self._label13)
		self._groupBox1.Controls.Add(self._label11)
		self._groupBox1.Controls.Add(self._label12)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label10)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label9)
		self._groupBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 149)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(306, 172)
		self._groupBox1.TabIndex = 17
		self._groupBox1.TabStop = False
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.LightPink
		self._label13.Location = System.Drawing.Point(83, 115)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 17
		self._label13.Click += self.Label13Click
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.LightPink
		self._label14.Location = System.Drawing.Point(87, 144)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 18
		self._label14.Click += self.Label14Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.ClientSize = System.Drawing.Size(493, 333)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog58t"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		Price = int(self._textBox1.Text)
		Amount = int(self._textBox2.Text)
		Change = Amount - Price
		Dollars =
		Dollars =
		Dimes = 
		Dimes = 
		Nickles = 
		Pennies = 
		
		
		self._label4.Text = str(Change)
		self._label10.Text = str(Dollars)
		self._label11.Text = str(Quarters)
		self._label12.Text = str(Dimes)
		self._label13.Text = str(Nickels)
		self._label14.Text = str(Pennies)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""

	def Button3Click(self, sender, e):
		Applicaton.Exit()

	def TextBox1TextChanged(self, sender, e):
		pass

	def TextBox2TextChanged(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label10Click(self, sender, e):
		pass

	def Label11Click(self, sender, e):
		pass

	def Label12Click(self, sender, e):
		pass

	def Label13Click(self, sender, e):
		pass

	def Label14Click(self, sender, e):
		pass
	
	float # decimal