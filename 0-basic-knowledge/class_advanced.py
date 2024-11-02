class person:
    person_number = 0 # you can define something in the class body
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.person_number += 1
    
    def greet(self, name, greeting):
        print("%s is saying %s to %s" % (self.name, greeting, name))
    
    def __get_sex(self): # "__" will make this function private
        print(self.sex)
        
tmp = person("123", 100, "male")
tmp.greet("dmyjqwdy", "hi")
# tmp.__get_sex() Error!
# but this will make it public:
tmp._person__get_sex() # "_Classname_privatefunction"


class Filter:
    def __init__(self):
        self.blocked = []
    
    def add(self, item):
        self.blocked.append(item)
    
    def get(self, container):
        print([x for x in container if x not in self.blocked])

f = Filter()
f.add(1)
f.add(2)
f.add(3)
f.get([1, 2, 4, 5, 6, 7])

class Bird:
    def __init__(self):
        self.hungry = False
        self.song = "hello"

    def sing(self):
        print(self.song)

class NewBird(Bird):
    def __init__(self):
        super().__init__() # use father class's construct function