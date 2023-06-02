class Greeting:
    name=""
    def say_hello_world(self):
        print("Hello World")

    def say_hello(self,name):
        print(f"Hello {name}")

    def say_hello_name(self):
        print(f"Hello {self.name}")

    def __str__(self):
        return "This is a Great Class"
        # No need of obj to print
    
    # def __init__(self):
    #     print("Constructor is envoked")
    # print("Class obj is envoked")

    def __init__(self,name):
        print("Constructor is envoked")
        self.name=name


obj = Greeting("Shouvik")
obj.say_hello_name()


# obj.name="Shouvik"
# obj.say_hello_name()

# print(obj.name)

# Location of class
# print(obj)

# obj.say_hello_world()
# obj.say_hello("Shouvik")