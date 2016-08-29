s = 'tim menzies'
def right_justify(s):
	value = len(s)
	remainder = 70 - len(s)
	print (' ' * remainder + s)
right_justify(s)