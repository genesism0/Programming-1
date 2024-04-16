import math
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
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.HotTrack
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(343, 121)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSkyBlue
		self._button1.Location = System.Drawing.Point(12, 139)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(98, 32)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSkyBlue
		self._button2.Location = System.Drawing.Point(138, 138)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(98, 33)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightSkyBlue
		self._button3.Location = System.Drawing.Point(257, 139)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(98, 32)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DodgerBlue
		self.ClientSize = System.Drawing.Size(367, 176)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number" + "\t" "Square" + "\t" "Square Root" + "\t" "Cube" + "\t" "4th Root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 20+1):
			square = num**2
			sq = math.sqrt(num)
			sq = round(sq, 4)
			cube = num**3
			Froot = sq**4
			Froot = round(Froot, 4)
			cal = str(num) + "\t" + str(square) + "\t" + str(sq) + "\t" + str(cube) + "\t" + str(Froot)
			self._listBox1.Items.Add(cal)
			

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()