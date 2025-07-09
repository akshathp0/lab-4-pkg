from shapes import Square, Circle
from utils import area_stats

square1 = Square(5) # square with sidelength of 5

circle1 = Circle(5) # circle with radius of 5

print(f"Square 1 area is: {square1.area()}")
print(f"Circle 1 area is: {circle1.area()}")

print(f"Area stats: {area_stats(square1, circle1)}")