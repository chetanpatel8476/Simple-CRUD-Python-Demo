from colored import fg, bg, attr

class Color:

	def setColor(self,color):
		if color == 'green':
			return fg(2)
		elif color == 'red':
			return fg(1)
		elif color == 'white':
			return fg(15)
		elif color == 'blue':
			return fg(4)
		elif color == 'orange':
			return fg(208)
		elif color == 'dark_green':
			return fg(22)
	
