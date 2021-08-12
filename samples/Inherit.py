class Father():#父类一
    def display(self, name):
        self.name = name
        print('Father name is', self.name)

class Mother():#父类二
    def display(self, name):
        self.name = name
        print('Mother name is', self.name)

#子类继承Father, Mother
class Child(Father, Mother):
    pass

class Son(Father): #子类继承Father
    pass

print(Child.__name__, '类, 继承两个基类')
for item in Child.__bases__:
    print(item)

Tom = Son()#子类实例，只有一个父类
Tom.display('Eric')
print(Son.__name__,'类，一个父类')
print(Son.__bases__)
Son.__bases__ = (Mother,)
Tom.display('Judy')
print(Son.__bases__)