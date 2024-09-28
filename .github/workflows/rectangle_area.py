# rectangle_area.py

def calculate_area(width, height):
    """Returns the area of a rectangle given width and height."""
    return width * height

if __name__ == "__main__":
    width = 5
    height = 10
    print(f"The area of a rectangle with width {width} and height {height} is {calculate_area(width, height)}")
