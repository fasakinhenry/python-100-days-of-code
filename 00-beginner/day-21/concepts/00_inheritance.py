# Learn about inheritance
class Animal:
    def __init__(self) -> None:
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# Create a child class that inherits from the Animal Class
class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("moving under water")


# Test out the functionalities of the child class
nemo = Fish()
nemo.breathe()
print(nemo.num_of_eyes)
