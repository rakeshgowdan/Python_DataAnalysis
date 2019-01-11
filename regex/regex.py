import re
pattern=re.compile("[a-z]")
string=pattern.match("hello world")
if(string):
	print(string.group())
	print(string.start(),string.end())