#Done by Sekharan Natarajan (200110398) smnatara

import utest
from sekhar import uppercase,uppercase_error
import who2
import who3

TEST_LIST = ["string1","string2","string with space","UPPERCASESTRING"]
@utest.ok
def test_capitalize():
	print "# Check if uppercase(\"string\")==\"STRING\""
	assert uppercase("string")=="STRING", "Not capitalized, Test failed"

@utest.ok
def test_capitalize_inbuilt():
	print "# Checking for " + ",".join(TEST_LIST)
	for str in TEST_LIST:
		assert str.upper()==uppercase(str),"Failed for " + str + " -->Expected " + str.upper() +" Got "+uppercase(str)

@utest.ok
def test_capitalize_inbuilt2():
	print "# Checking for " + ",".join(TEST_LIST)
	for str in TEST_LIST:
		assert str.upper()==uppercase_error(str),"Failed for " + str + " -->Expected " + str.upper() +" Got "+uppercase_error(str) 