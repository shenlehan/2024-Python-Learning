import re

pat = "[, ]+"
obj = re.compile(pat)
print(obj.split('aaa,   ,   bb,, ,,     ,,   ,,c,      ,d'))

pat = '[a-zA-Z]+'
obj = re.compile(pat)
print(obj.findall('Hello World~~!!'))