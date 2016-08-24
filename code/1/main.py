#Done by Sekharan Natarajan (200110398) smnatara

import utest
from sekhar import uppercase,uppercase_error
from neha import lowercase
from khan import capitalize

TEST_LIST = ["string1","string2","string with space","UPPERCASESTRING"]
@utest.ok
def test_uppercase():
	print "# Check if uppercase(\"string\")==\"STRING\""
	assert uppercase("string")=="STRING", "Not capitalized, Test failed"

@utest.ok
def test_uppercase_inbuilt():
	print "# Checking for " + ",".join(TEST_LIST)
	for str in TEST_LIST:
		assert str.upper()==uppercase(str),"Failed for " + str + " -->Expected " + str.upper() +" Got "+uppercase(str)

@utest.ok
def test_lowercase_inbuilt():
	print "# Checking for " + ",".join(TEST_LIST)
	for str in TEST_LIST:
		assert str.lower()==lowercase(str),"Failed for " + str + " -->Expected " + str.lower() +" Got "+lowercase(str)


@utest.ok
def test_capitalize_inbuilt():
	print "# Checking for " + ",".join(TEST_LIST)
	for str in TEST_LIST:
		assert str.capitalize()==capitalize(str),"Failed for " + str + " -->Expected " + str.capitalize() +" Got "+capitalize(str)


##Failure case
@utest.ok
def test_uppercase_inbuilt2():
	print "# Checking for " + ",".join(TEST_LIST)
	for str in TEST_LIST:
		assert str.upper()==uppercase_error(str),"Failed for " + str + " -->Expected " + str.upper() +" Got "+uppercase_error(str)


utest.oks()