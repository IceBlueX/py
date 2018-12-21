class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat ...')


class Cat(Animal):
    def run(self):
        print('cat is running...')

    def eat(self):
        print('Eating meat ...')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

class Timer(object):
    def run(self):
        print('Start...')

dog=Dog()
dog.run()

cat=Cat()
cat.run()

