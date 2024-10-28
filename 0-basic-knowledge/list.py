alphabeta = ['a', 'b', 'c', 'd', 'e']
print(alphabeta) # 会打印出包括 [] 和 ' '

print(alphabeta[-1]) # 打印出最后一个元素
print(alphabeta[-2]) # 打印出倒数第二个元素
print(alphabeta[-3]) # 打印出倒数第三个元素

alphabeta.append('f')
print(alphabeta)

alphabeta.insert(1, 'x') # 在对应位置插入
print(alphabeta)

letter = alphabeta.pop() # 获得尾部的值并弹出尾部
print(alphabeta, letter)

del alphabeta[1]
print(alphabeta)

alphabeta.remove('c') # 查找删除
print(alphabeta)

alphabeta.sort(reverse = True) # 排序（有 reverse=True 则降序）
print(alphabeta)

fruit = ['apple', 'orange', 'watermelon', 'banana', 'pineapple', 'rabbit', 'tiger', 'pear']
print(sorted(fruit)) # 临时排序
print(sorted(fruit, reverse = True))
print(fruit)

fruit.reverse()
print(fruit)

print(len(fruit))

for item in fruit:
    print(item)

print(item) # python 中循环变量似乎会被保存下来，值就是最后一个

for i in range(1, 10):
    print(i) # 结果应当是 1 - 9，因为 range(x, y) 是 [x, y)

numbers = list(range(1, 6)) # 创建一个 1 - 5 的列表
print(numbers)

even_num = list(range(2, 12, 2)) # 最后一位是步长
print(even_num)

# 列表推导式
square = [value ** 2 for value in range(1, 11)]
print(square)

# 切片
print(square[1: 4]) # 也是 [x, y)

# 复制列表
list1 = [1, 2, 3, 4, 5]
list2 = list1[:] # 这样相当于传值复制
list3 = list1 # 这个相当于传址复制
print(list1)
print(list2)

print('')
list3[1] = 100
print(list1)
print(list3)

a = []
for i in range(1, 11):
    a.append(i)
n = len(a)
print(n, a)