from shapes import Rectangle, Circle, Triangle
from utils import cm2_to_m2, compare_areas

def welcome():
    """
    Print a welcome message and explain available shapes.
    """
    print("Welcome to the Shape Toolkit!")
    print("You can create rectangles, circles, and triangles.")
    print("Enter dimensions to see area and description.")

def main():
    welcome()
    while True:
        print("\nChoose a shape to create:")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            w = float(input("Width: "))
            h = float(input("Height: "))
            rect = Rectangle(w, h)
            rect.describe()
            print(f"Area in m^2: {cm2_to_m2(rect.area()):.4f}")
        elif choice == '2':
            r = float(input("Radius: "))
            circ = Circle(r)
            circ.describe()
            print(f"Area in m^2: {cm2_to_m2(circ.area()):.4f}")
        elif choice == '3':
            b = float(input("Base: "))
            h = float(input("Height: "))
            tri = Triangle(b, h)
            tri.describe()
            print(f"Area in m^2: {cm2_to_m2(tri.area()):.4f}")
        elif choice == '4':
            print("Are you a tomato?")
            break
        else:
            print("Bro. Follow the instructions.")

if __name__ == "__main__":
    main()
