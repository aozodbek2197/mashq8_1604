# 1-mashq
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

class Factory:
    def get_animal(self, type):
        if type == "dog":
            return Dog()
        return Cat()
# 2-mashq
class Engine:
    def run(self):
        print("Engine ishladi")

class Car:
    def __init__(self, engine):
        self.engine = engine

e = Engine()
c = Car(e)
c.engine.run()
# 3-mashq
class Subject:
    def __init__(self):
        self.observers = []

    def add(self, obs):
        self.observers.append(obs)

    def notify(self):
        for o in self.observers:
            o.update()

class Observer:
    def update(self):
        print("Yangilandi")
# 4-mashq
class Cache:
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
# 5-mashq
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)
