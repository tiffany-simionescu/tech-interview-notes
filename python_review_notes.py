# The 4 Pillars of OOP:
# Encapsulation - hiding the implementation details of an object
# Abstraction - level of detail appropriate to a task
# Inheritence - the family tree
# Polymorphism - treat a class differently depending on which subclass is implemented

# init - constructor method for class, a special method
# str - special method returns a string representation of an object (debugging)
# repr - special method similar to str. returns one of the ways possible to create the object

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.__private_name = "This is private"

my_point = Point(1, 2)
my_point.__private_name #(won't work)
my_point._Point__private_name  #(will work)


# Instances of class:
class Counter():
    count = 0
    def __init__(self):
        Counter.count += 1
    def exclaim(self):
        print("I'm a Counter!")
    @classmethod
    def children(cls):
        print(f"Counter class has {cls.count} instances that have been created")

counter_one = Counter()
counter_two = Counter()
counter_three = Counter()
Counter.children()
# Counter class has 3 instances that have been created


# super:
class Student():
    def __init__(self, name):
        self.name = name

class Graduate(Student):
    def __init__(self, name, graduation_date):
        super().__init__(name)
        self.graduation_date = graduation_date

