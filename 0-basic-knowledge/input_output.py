message = 'hello world'
print(message)
print(message.title())
print(message.upper())

text1 = 'hello world'
text2 = '123'
message = f"{text1} {text2}" # 在一个字符串中添加变量
print(message)
print(message.rstrip())

print(__file__, '\n') # '\n' 会导致额外的一行空行
print(message.removeprefix('hello '))