from string import Template
s = [1, "strssss", 1.003, "1003", ["slh", "nju"]]

for i in s:
    print(i)

# similar to printf
print("This is a number: %f and this is a string: %s\n" % (s[2], s[3]))

#using template
print(Template("Hello, $name, nice to meet you for $time times").substitute(name="qwq", time=123))

s = "hello, my name is dmyjqwdy from nanjing university."
print(s.title()) # capitalize each word
print(s.upper()) # all capitalize
print()

s1 = "{}, {} and {}".format("slh", "nju", "sz")
print(s1)
s2 = "{2}, {1} and {0}".format("slh", "nju", "sz")
print(s2)
s3 = "{city}, {name} and {school}".format(name = "slh", school = "nju", city = "sz")
print(s3)

from math import pi
s4 = "{name} is approximately {value:.2f}.".format(value=pi, name="π")
print(s4)
print()

print("{pi!s} {pi!r} {pi!a}".format(pi="π"))
# !ch 是格式指令，s表示转换为普通字符串，r表示python表示的字符串，a表示ascii码
print()

print("{π:10.5f}".format(π=pi))
# 10.5f 就是c语言printf的格式
# : 代替了 % 的作用，也可以这么写
print("{:10.5f}".format(pi))

dic = {
    1: [1, 2], # it could be anything you want, so powerful
    2: [3, 4, 5],
    3: "Hello"
}
print(dic[1])

for i, j in dic.items():
    print(f"key is %d and value is {j}" % (i))

for i in dic: # print key value
    print(i)

print(dic.values())

# some auguments to print():
print("Hello", "world", sep='*' * 10, end="")
# sep is the seprating character
# end is the ending charater, and it's '\n' for default
print("hello again")