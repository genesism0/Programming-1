﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.num1 = 0
		self.num2 = 0
		self.num3 = 0
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("SlotMachine.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._pictureBox5 = System.Windows.Forms.PictureBox()
		self._pictureBox6 = System.Windows.Forms.PictureBox()
		self._pictureBox7 = System.Windows.Forms.PictureBox()
		self._pictureBox8 = System.Windows.Forms.PictureBox()
		self._pictureBox9 = System.Windows.Forms.PictureBox()
		self._pictureBox10 = System.Windows.Forms.PictureBox()
		self._pictureBox11 = System.Windows.Forms.PictureBox()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self._pictureBox5.BeginInit()
		self._pictureBox6.BeginInit()
		self._pictureBox7.BeginInit()
		self._pictureBox8.BeginInit()
		self._pictureBox9.BeginInit()
		self._pictureBox10.BeginInit()
		self._pictureBox11.BeginInit()
		self.SuspendLayout()
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.Color.White
		self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox1.Location = System.Drawing.Point(9, 7)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(101, 144)
		self._pictureBox1.TabIndex = 0
		self._pictureBox1.TabStop = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackColor = System.Drawing.Color.White
		self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox2.Location = System.Drawing.Point(128, 7)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(100, 144)
		self._pictureBox2.TabIndex = 1
		self._pictureBox2.TabStop = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackColor = System.Drawing.Color.White
		self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox3.Location = System.Drawing.Point(244, 7)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(96, 144)
		self._pictureBox3.TabIndex = 2
		self._pictureBox3.TabStop = False
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackColor = System.Drawing.Color.White
		self._pictureBox4.BackgroundImage = resources.GetObject("pictureBox4.BackgroundImage")
		self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox4.Location = System.Drawing.Point(9, 157)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(331, 174)
		self._pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox4.TabIndex = 3
		self._pictureBox4.TabStop = False
		self._pictureBox4.Visible = False
		# 
		# button1
		# 
		self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button1.Location = System.Drawing.Point(356, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(141, 161)
		self._button1.TabIndex = 4
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(356, 179)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(141, 34)
		self._button2.TabIndex = 5
		self._button2.Text = "Pickpocket"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SkyBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(356, 240)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(55, 22)
		self._label1.TabIndex = 6
		self._label1.Text = "Bet:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(411, 238)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(86, 23)
		self._textBox1.TabIndex = 7
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SkyBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(356, 268)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(55, 23)
		self._label2.TabIndex = 8
		self._label2.Text = "Cash:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DodgerBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(411, 269)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(86, 23)
		self._label3.TabIndex = 9
		self._label3.Text = "100"
		# 
		# pictureBox5
		# 
		self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
		self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox5.Location = System.Drawing.Point(23, 170)
		self._pictureBox5.Name = "pictureBox5"
		self._pictureBox5.Size = System.Drawing.Size(44, 43)
		self._pictureBox5.TabIndex = 11
		self._pictureBox5.TabStop = False
		self._pictureBox5.Visible = False
		# 
		# pictureBox6
		# 
		self._pictureBox6.BackgroundImage = resources.GetObject("pictureBox6.BackgroundImage")
		self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox6.Location = System.Drawing.Point(73, 170)
		self._pictureBox6.Name = "pictureBox6"
		self._pictureBox6.Size = System.Drawing.Size(44, 43)
		self._pictureBox6.TabIndex = 12
		self._pictureBox6.TabStop = False
		self._pictureBox6.Visible = False
		# 
		# pictureBox7
		# 
		self._pictureBox7.BackgroundImage = resources.GetObject("pictureBox7.BackgroundImage")
		self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox7.Location = System.Drawing.Point(123, 170)
		self._pictureBox7.Name = "pictureBox7"
		self._pictureBox7.Size = System.Drawing.Size(44, 43)
		self._pictureBox7.TabIndex = 13
		self._pictureBox7.TabStop = False
		self._pictureBox7.Visible = False
		# 
		# pictureBox8
		# 
		self._pictureBox8.BackgroundImage = resources.GetObject("pictureBox8.BackgroundImage")
		self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox8.Location = System.Drawing.Point(173, 170)
		self._pictureBox8.Name = "pictureBox8"
		self._pictureBox8.Size = System.Drawing.Size(44, 43)
		self._pictureBox8.TabIndex = 14
		self._pictureBox8.TabStop = False
		self._pictureBox8.Visible = False
		# 
		# pictureBox9
		# 
		self._pictureBox9.BackgroundImage = resources.GetObject("pictureBox9.BackgroundImage")
		self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox9.Location = System.Drawing.Point(223, 170)
		self._pictureBox9.Name = "pictureBox9"
		self._pictureBox9.Size = System.Drawing.Size(45, 43)
		self._pictureBox9.TabIndex = 15
		self._pictureBox9.TabStop = False
		self._pictureBox9.Visible = False
		# 
		# pictureBox10
		# 
		self._pictureBox10.BackgroundImage = resources.GetObject("pictureBox10.BackgroundImage")
		self._pictureBox10.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox10.Location = System.Drawing.Point(73, 219)
		self._pictureBox10.Name = "pictureBox10"
		self._pictureBox10.Size = System.Drawing.Size(44, 43)
		self._pictureBox10.TabIndex = 16
		self._pictureBox10.TabStop = False
		self._pictureBox10.Visible = False
		# 
		# pictureBox11
		# 
		self._pictureBox11.BackgroundImage = resources.GetObject("pictureBox11.BackgroundImage")
		self._pictureBox11.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox11.Location = System.Drawing.Point(23, 219)
		self._pictureBox11.Name = "pictureBox11"
		self._pictureBox11.Size = System.Drawing.Size(44, 43)
		self._pictureBox11.TabIndex = 17
		self._pictureBox11.TabStop = False
		self._pictureBox11.Visible = False
		# 
		# progressBar1
		# 
		self._progressBar1.BackColor = System.Drawing.Color.DodgerBlue
		self._progressBar1.Location = System.Drawing.Point(356, 308)
		self._progressBar1.Maximum = 15000
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(141, 23)
		self._progressBar1.TabIndex = 18
		# 
		# timer1
		# 
		self._timer1.Tick += self.Timer1Tick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightBlue
		self.ClientSize = System.Drawing.Size(509, 343)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._pictureBox11)
		self.Controls.Add(self._pictureBox10)
		self.Controls.Add(self._pictureBox9)
		self.Controls.Add(self._pictureBox8)
		self.Controls.Add(self._pictureBox7)
		self.Controls.Add(self._pictureBox6)
		self.Controls.Add(self._pictureBox5)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Name = "MainForm"
		self.Text = "SlotMachine"
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self._pictureBox5.EndInit()
		self._pictureBox6.EndInit()
		self._pictureBox7.EndInit()
		self._pictureBox8.EndInit()
		self._pictureBox9.EndInit()
		self._pictureBox10.EndInit()
		self._pictureBox11.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button2Click(self, sender, e):
		rnd = System.Random()
		money = rnd.Next(1, 51)
		if money > 25:
			MessageBox.Show("You failed to steal money!")
		else:
			cmoney = float(self._label3.Text)
			self._label3.Text = str(round(cmoney + money, 2))
		pass

	def Button1Click(self, sender, e):
		im1 = self._pictureBox5.BackgroundImage
		im2 = self._pictureBox6.BackgroundImage
		im3 = self._pictureBox7.BackgroundImage
		im4 = self._pictureBox8.BackgroundImage
		im5 = self._pictureBox9.BackgroundImage
		levOff = self._pictureBox10.BackgroundImage
		levOn = self._pictureBox11.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		# Copy these (above) into timerTick
		
		if self._textBox1.Text == "":
			MessageBox.Show("You must enter an amount to bet first!")
			return
		
		money = float(self._label3.Text)
		bet = float(self._textBox1.Text)
		money2 = money - bet
		
		if money == 0:
			MessageBox.Show("You have no money!")
		elif bet < 1:
			MessageBox.Show("You must bet at least 1 dollar!")
		elif bet > money and bet > money2:
			MessageBox.Show("You dont have enough money!")
		else:
			self._button1.BackgroundImage = levOn
			self._pictureBox4.Visible = True
			self._timer1.Enabled = True
			self._label3.Text = str(round(money2, 2))
			self._progressBar1.Value = 0
			
			num1 = self.num1
			num2 = self.num2
			num3 = self.num3
			
			if num1 == 1 and num2 == 1 and num3 == 1:
				money2 += bet * 2
				
			if num1 == 2 and num2 == 2 and num3 == 2:
				money2 += bet * 20
				
			if num1 == 3 and num2 == 3 and num3 == 3:
				money2 += bet * 50
			
			if num1 ==  4 and num2 == 4 and num3 == 4:
				money2 += bet * 75
		
			if num1 == 5 and num2 == 5 and num3 == 5:
				money2 += bet * 100
				
		# TODO: Check if num1, num2, and num3 = 3, 4, and 5
		# and multiply bet by whatever you want
		
			self.num1 = 0
			self.num2 = 0 
			self.num3 = 0
			self._label3.Text = str(round(money2, 2))
			
			if money2 <= 0:
				MessageBox.Show("You ran out of cash!")
				
				

	def Timer1Tick(self, sender, e):
		im1 = self._pictureBox5.BackgroundImage
		im2 = self._pictureBox6.BackgroundImage
		im3 = self._pictureBox7.BackgroundImage
		im4 = self._pictureBox8.BackgroundImage
		im5 = self._pictureBox9.BackgroundImage
		levOff = self._pictureBox10.BackgroundImage
		levOn = self._pictureBox11.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		# Copied from Button1Click
		
		pb1 = self._pictureBox1
		pb2 = self._pictureBox2
		pb3 = self._pictureBox3
		
		for lcv in range(0, 1000):
			num1 = rnd.Next(1, 6) # Generate a # between 1 & 5
			num2 = rnd.Next(1, 6)
			num3 = rnd.Next(1, 6)
		
			# Copy/paste this for num2/pb2 and num3/pb3
			if num1 == 1:
				pb1.BackgroundImage = im1
			elif num1 ==2:
				pb1.BackgroundImage = im2
			elif num1 == 3:
				pb1.BackgroundImage = im3
			elif num1 == 4:
				pb1.BackgroundImage = im4
			elif num1 == 5:
				pb1.BackgroundImage = im5
			
			if num2 == 1:
				pb2.BackgroundImage = im1
			elif num2 == 2:
				pb2.BackgroundImage = im2
			elif num2 == 3:
				pb2.BackgroundImage = im3
			elif num2 == 4:
				pb2.BackgroundImage = im4
			elif num2 == 5:
				pb2.BackgroundImage = im5
				
			if num3 == 1:
				pb3.BackgroundImage = im1
			elif num3 == 2:
				pb3.BackgroundImage = im2
			elif num3 == 3:
				pb3.BackgroundImage = im3
			elif num3 == 4:
				pb3.BackgroundImage = im4
			elif num3 == 5:
				pb3.BackgroundImage = im5
				
			if num4 == 1:
				pb4.BackgroundImage = im1
			elif num4 == 2:
				pb4.BackgroundImage = im2
			elif num4 == 3:
				pb4.BackgroundImage = im3
			elif num4 == 4:
				pb4.BackgroundImage = im4
			elif num4 == 5:
				pb4.BackgroundImage = im5
				
			if num5 == 1:
				pb5.BackgroundImage = im1
			elif num5 == 2:
				pb5.BackgroundImage = im2
			elif num5 == 3:
				pb5.BackgroundImage = im3
			elif num5 == 4:
				pb5.BackgroundImage = im4
			elif num5 == 5:
				pb5.BackgroundImage = im5
		
			self._progressBar1.Increment(1)
			if self._progressBar1.Value == self._progressBox.Maximum:
				self._timer1.Enabled = False
				self._pictureBox4.Visible = False
				self._button1.BackgroundImage = levOff
			
		pass