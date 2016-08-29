#Module to convert a given ascii string to it lowercase equivalent
def lowercase(str):
	new_str = list(str)
	for i in range(0,len(str)):
		#print new_str[i]
		if (ord(str[i]) >= ord('A')) and (ord(str[i])<=ord('Z')):
			new_str[i] = chr(ord(new_str[i])+32)
	return "".join(new_str)