from pathlib import Path # Path 函数可以访问文件位置

path = Path('read_files.py') # 相对路径，要求当前文件和目标文件在同一个文件夹内
print(path)

# path = Path('read_files.py').resolve() # 绝对路径，要求当前文件和目标文件在同一个文件夹内
# print(path)

contents = path.read_text() # 把 path 对应的文件中的内容以字符串形式读取，不过末尾会多一个换行
print(contents)

print('*****************************')

lines = contents.splitlines() # 拆成行的形式
for i in lines:
    print(i)