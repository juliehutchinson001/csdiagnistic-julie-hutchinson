class Car:

def __init__(self, color):
self.num_wheels = 4
self.make = 'chrisler'
self.model = 'PT Cruiser'
self.color = color
self.speed = 100

def honk(self):
print("Beep Beep!")

def description(self):
print('{}:{}, {}:{}, {}:{}, {}:{}, {}:{}'.format('make', self.make, 'model', self.model, 'color', self.color, 'speed', self.speed, 'num_wheels', self.num_wheels))

