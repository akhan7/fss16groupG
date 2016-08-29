#Module to convert a given ascii string to it uppercase equivalent
def uppercase(str):
	new_str = list(str)
	for i in range(0,len(str)):
		#print new_str[i]
		if (ord(str[i]) >= ord('a')) and (ord(str[i])<=ord('z')):
			new_str[i] = chr(ord(new_str[i])-32)
	return "".join(new_str)

def uppercase_error(str):
	new_str = list(str)
	for i in range(0,len(str)):
		#print new_str[i]
		if (ord(str[i]) >= ord('a')) and (ord(str[i])<=ord('z')):
			new_str[i] = chr(ord(new_str[i])-32)
		else:
			new_str=' '
	return "".join(new_str)