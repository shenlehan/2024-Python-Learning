watermelon = {
    'color' : 'red & green',
    'taste' : 'sweet',
    'price' : '1.99$'
}

orgin = watermelon.get('origin')
print(orgin) # 输出 None，但不会报错
# print(watermelon['origin']) 则会报错

for k, v in watermelon.items(): # 既遍历键，也遍历值
    print(f"{k}, {v}") # 按照 k, v 定义顺序获取 键 - 值对

print('')
for k in watermelon.keys(): # 仅遍历键
    print(f"{k} is a key")

print('')
for k in watermelon: # 默认情况也是遍历键
    print(f"{k} is a key")


print('')
for v in watermelon.values(): # 仅遍历值
    print(f"{v} is a value")

if 'color' in watermelon.keys(): # 实际上它们构成一个 list，可以直接遍历
    print('Yes')

alphabet = {
    'x': 1,
    'y': 2,
    'z': 2,
    'p': 3
}

print(alphabet.values())
for i in set(alphabet.values()): # 集合 set 去重
    print(i)

# 定义一个集合
languages = {"C", "C++", "Python", "Java", "Python"}
print(languages) # 自动去重

print(alphabet)

people = {} # 定义一个空字典
people['123'] = 123 # 直接添加
people['456'] = 456

for k, v in people.items():
    print(f"{k}'s value is {v}")