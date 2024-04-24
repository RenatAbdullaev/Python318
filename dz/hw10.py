class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop

    def print_info(self):
        print(f"Name: {self.name}")
        print("Laptop Info:")
        print(f"Model: {self.laptop.model}")
        print(f"Processor: {self.laptop.processor}")
        print(f"Memory: {self.laptop.memory}")


class Laptop:
    def __init__(self, model, processor, memory):
        self.model = model
        self.processor = processor
        self.memory = memory


laptop1 = Laptop("hp", "i7", 16)
student1 = Student("Roman", laptop1)
student1.print_info()

laptop2 = Laptop("hp", "i7", 16)
student2 = Student("Vladimir", laptop2)
student2.print_info()
