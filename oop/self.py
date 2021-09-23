# URL : https://www.askpython.com/python/python-self-variable

'''
    Python self variable is used to bind the instance of the class to the instance method. 
    We have to explicitly declare it as the first method argument to access 
    the instance variables and methods. This variable is used only with the instance methods.

    Python self variable is not a reserved keyword. But, it’s the best practice and convention 
    to use the variable name as “self” to refer to the instance
'''

class Dog:
 
    def __init__(self, breed):
        self.breed = breed
 
    def bark(self):
        print(f'{self.breed} is barking.')
 
 
d = Dog('Labrador')
d.bark()

# OUTPUT : Labrador is barking.

'''
    1. The __init__() function is defined with two variables 
    but when we are creating the Dog instance, we have to provide only one argument. 
    The “self” is automatically assigned to the newly created instance of Dog class.

    2. The bark() method has only one argument – “self” – which gets bind to the Dog 
    instance that calls this method
'''

# 2. CAN WE SKIP THE "SELF" VARIABLE ?

class Dog:
 
    def bark():
        print('Barking')
 
d = Dog()
print("Done") # the code will run up to this point


d.bark() # Here the code will raise an error because bark will be passed 
         # a reference to the instance of the Dog that will call it

Dog.bark() # This will work as we are accessing bark() through the class reference


# 3. CLASS METHOD AND STATIC METHOD

class Dog:
 
    def __init__(self, breed):
        self.breed = breed
 
    @classmethod
    def walk(cls):
        print('Dog is Walking')
 
    # instance method
    def bark(self):
        print(f'{self.breed} is barking.')
 
    @staticmethod
    def add(x, y):
        return x + y
 
 
Dog.walk()
d = Dog('Labrador')
d.bark()
print(Dog.add(10, 20))

# 4. SELF VARIABLE IS BOUND TO THE CURRENT INSTANCE

'''
    The self variable gives us access to the current instance properties
'''

class Dog:
 
    def __init__(self, b):
        self.breed = b
 
    def bark(self):
        print(f'{self.breed} is Barking.')
 
 
d1 = Dog('Labrador')
d2 = Dog('Husky')
 
d1.bark() # output : Labrador is Barking.
d2.bark() # output : Husky is Barking.

