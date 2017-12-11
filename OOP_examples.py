#Solution Problem 10: object oriented programming
class Car:

def __init__(self, color):
self.num_wheels = 4
self.make = 'chrisler'
self.model = 'PT Cruiser'
self.color = color
self.speed = 100

def sound(self):
print("Beep Beep!")

def description(self):
print('{}:{}, {}:{}, {}:{}, {}:{}, {}:{}'.format('make', self.make, 'model', self.model, 'color', self.color, 'speed', self.speed, 'num_wheels', self.num_wheels))



#Solution Problem 11: Inheritance

Inheritance is a method of grouping data in an efficient
manner with different purposes and benefits
for programmers since it allows to avoid repeating
the same code over and over. Programmers, through
inheritance, are able to import, from a different
code a section that might be needed.


#Solution Problem 12 Superclasses

class Automobile(object):
    def __init__(self, color):
        self.color = color
        self.model = "Honda"

    def sound(self):
        print "Bee Beep!"

    def description(self):
        print vars(self)

class Motorcycle(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.wheelNum = 2
        self.make = "Ducati?"
        self.top_speed = 70

class Car(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.wheelNum = 4
        self.make = "Accord?"
        self.top_speed = 100

class SemiTruck(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.wheelNum = 16
        self.make = "Big Rig?"
        self.top_speed = 60

if __name__ == "__main__":
    test1 = Car("Blue")
    print test1.color
    print test1.top_speed
    test1.sound()
    test1.description()

    test2 = Motorcycle("Black")
    print test2.color
    print test2.top_speed
    test2.sound()
    test2.description()
