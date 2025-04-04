import math

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = 0.5 * base * height
        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = width * height
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = math.pi * radius ** 2
        else:
            print("Unknown shape!")
            continue
        print(f"The area is {area:.6f}")

if __name__ == "__main__":
    main()
