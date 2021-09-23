# URL : https://www.askpython.com/python/oops/python-class-constructor-init-function

# Python Class Constructor – Python __init__() Function

# SYNTAX : def __init__(self, [arguments])

''' 
1. The first argument refers to the current object. 
    It binds the instance to the init() method. 
    It’s usually named “self” to follow the naming convention. 
    You can read more about it at Python self variable

2. The init() method arguments are optional. We can define a constructor 
   with any number of arguments.
'''

# 1. CLASS WITH NO CONSTRUCTOR :

'''
    In the case where the constructor is not defined,
    the superclass constructor is called to intialize the the instance 
    of the class and in this case its the constructor of the class 'object'
    which is the super class of all the classes in python
'''

# first example :
class Data:
    pass

d = Data()
print(type(d))  # <class '__main__.Data'>

# second example : 
class BaseData:
 
    def __init__(self, i):
        print(f'BaseData Constructor with argument {i}')
        self.id = i
 
 
class Data(BaseData):
    pass
 
 
d = Data(10)
print(type(d))

# 2. SIMPLE CONSTRUCTOR WITH NO ARGUMENT :

class Data1:
    count = 0
 
    def __init__(self):
        print('Data1 Constructor')
        Data1.count += 1
 
 
d1 = Data1()
d2 = Data1()
print("Data1 Object Count =", Data1.count)


# 3. CLASS CONSTRUCTOR WITH ARGUMENT

class Data2:
 
    def __init__(self, i, n):
        print('Data2 Constructor')
        self.id = i
        self.name = n
 
 
d2 = Data2(10, 'Secret')
print(f'Data ID is {d2.id} and Name is {d2.name}')

# 4. CLASS CONSTRUCTOR WITH INNHERITANCE

''''
    1. It's our responsability to call our superclass constructor
    2.We can either use the 'super()' or the superclass name to call the 
    'init()' method of the superclass
''''

class Person:
 
    def __init__(self, n):
        print('Person Constructor')
        self.name = n
 
 
class Employee(Person):
 
    def __init__(self, i, n):
        print('Employee Constructor')
        super().__init__(n)  # same as Person.__init__(self, n)
        self.id = i
 
 
emp = Employee(99, 'Pankaj')
print(f'Employee ID is {emp.id} and Name is {emp.name}')

# 5. CONSTRUCTOR CHAINING WITH MULTILEVEL INHERITANCE


class A:
 
    def __init__(self, a):
        print('A Constructor')
        self.var_a = a
 
 
class B(A):
 
    def __init__(self, a, b):
        super().__init__(a)
        print('B Constructor')
        self.var_b = b
 
 
class C(B):
 
    def __init__(self, a, b, c):
        super().__init__(a, b)
        print('C Constructor')
        self.var_c = c
 
 
c_obj = C(1, 2, 3)
print(f'c_obj var_a={c_obj.var_a}, var_b={c_obj.var_b}, var_c={c_obj.var_c}')


# 6. CONSTRUCTOR WITH INHERITANCE :

'''
    We cant use super() to access the constructor of superclass in case of
    multiple inheritance, the better approach would be to use the superclass
    name
'''

class A1:
    def __init__(self, a1):
        print('A1 Constructor')
        self.var_a1 = a1
 
 
class B1:
    def __init__(self, b1):
        print('B1 Constructor')
        self.var_b1 = b1
 
 
class C1(A1, B1):
    def __init__(self, a1, b1, c1):
        print('C1 Constructor')
        A1.__init__(self, a1)
        B1.__init__(self, b1)
        self.var_c1 = c1
 
 
c_obj = C1(1, 2, 3)
print(f'c_obj var_a={c_obj.var_a1}, var_b={c_obj.var_b1}, var_c={c_obj.var_c1}')


# 7. MULTIPLE DOESNT SUPPORT MULTIPLE INIT()

'''
    Python doesn’t support multiple constructors, unlike other popular object-oriented 
    programming languages such as Java.
    We can define multiple __init__() methods but the last one will override the earlier definitions
'''

class D:
 
    def __init__(self, x):
        print(f'Constructor 1 with argument {x}')
 
    # this will overwrite the above constructor definition
    def __init__(self, x, y):
        print(f'Constructor 1 with arguments {x}, {y}')
 
 
d1 = D(10, 20) # Constructor 1 with arguments 10, 20


# 8. PYTHON INIT() FUNCTION CANNOT RETURN SOMETHING

'''
    If we try to return a non-None value from the __init__() function, it will raise TypeError.
'''

class Data:
 
    def __init__(self, i):
        self.id = i
        return True
 
d = Data(10)

# OUTPUT : peError: __init__() should return None, not 'bool'


