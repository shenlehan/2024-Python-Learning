def func(a, b):
    print(a * 2, b + 1)

func(5, 10)
func(b = 5, a = 10) # 指定参数的值

# default parameters
def function(a, b, c = 1):
    print(a * b * c)

function(2, 3)

def get_formatted_name(first_name, last_name, middle_name = ''):
    # print(f"{fisrt_name} {middle_name} {last_name}".title())
    if middle_name: # 空字符串会被认为是 False
        print(f"{first_name} {middle_name} {last_name}".title())
    else:
        print(f"{first_name} {last_name}".title())

def get_pair(x, y):
    pair = {}
    pair[x] = y
    return pair

def make_pizza(*toppings): # * 会创建一个叫 toppings 的元组，可以接受任意数量的参数
    print(toppings)

def person(first, last, **user_info): # ** 会创建一个叫 user_info 的字典
    user_info['first'] = first
    user_info['last'] = last
    return user_info

# 调用时
slh = person('Lehan', 'Shen', school = 'Tsinghua University', age = 17)
print(slh)

import input