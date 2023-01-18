class A():
    def sound(self):
        pass

class B(A):
    def sound(self):
        print('Meow')

class C(A):
    def sound(self):
        print('WOw')

if __name__ == '__main__':
    a = A()
    a.sound()
    b = B()
    b.sound()