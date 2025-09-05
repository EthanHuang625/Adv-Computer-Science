
import math

class Rectangle:
   
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
     
        return self.width * self.height

    def describe(self) -> None:
        
        print(f"Rectangle: {self.width} x {self.height}, area = {self.area():.2f}")

class Circle:
  
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:

        return math.pi * self.radius ** 2

    def describe(self) -> None:
  
        print(f"Circle: radius = {self.radius}, area = {self.area():.2f}")

class Triangle:

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
    
        return 0.5 * self.base * self.height

    def describe(self) -> None:
     
        print(f"Triangle: base = {self.base}, height = {self.height}, area = {self.area():.2f}")
