class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the rectangle with length and width
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield length first, then width when iterating
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage of the class
if __name__ == '__main__':
    # Create an instance of Rectangle
    rect = Rectangle(10, 5)

    # Iterate over the instance and print the results
    for attribute in rect:
        print(attribute)
