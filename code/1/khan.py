#Module to capitalize an ascii string
from neha import lowercase
def capitalize(str):
	str = lowercase(str)
	new_str = list(str)
	for i in range(0,1):
		#print new_str[i]
		if (ord(str[i]) >= ord('a')) and (ord(str[i])<=ord('z')):
			new_str[i] = chr(ord(new_str[i])-32)

	return "".join(new_str)