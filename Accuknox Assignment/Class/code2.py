class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the length and width attributes
        self.length = length
        self.width = width

    def __iter__(self):
        # Create an iterator that yields each dictionary in the required format
        return iter([{'length': self.length}, {'width': self.width}])

# Create an instance of the Rectangle class with specific length and width
rectangle = Rectangle(10, 5)

# Iterate over the rectangle instance to get the required output
for attribute in rectangle:
    print(attribute)

