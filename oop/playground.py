class Data1:
    count = 0
 
    def __init__(self):
        print('Data1 Constructor')
        self.count += 1

class D:
 
    def __init__(self, x):
        print(f'Constructor 1 with argument {x}')
 
    # this will overwrite the above constructor definition
    def __init__(self, x, y):
        print(f'Constructor 1 with arguments {x}, {y}')

class Data:
 
    def __init__(self, i):
        self.id = i
        return True
 
class Dog:
 
    def bark():
        print('Barking')

if __name__ == '__main__':
    # d1 = Data1()
    # d2 = Data1()
    # print("Data1 Object Count =", Data1.count)
    # print("d1 Object Count =", d1.count)
    # print("d21 Object Count =", d2.count)

    # d = D(10,90)
    # d1 = Data(30)

    d = Dog()
    print("Done")
    d.bark()
    