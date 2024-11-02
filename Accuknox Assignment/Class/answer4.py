class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  # This helps keep track of the iteration state

    def __iter__(self):
        self._index = 0  # Reset the index every time we start a new iteration
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration  # Stop after two items

# This block will only run if the file is executed directly
if __name__ == "__main__":
    # Example of usage
    rect = Rectangle(10, 5)

    # Iterate over the rectangle instance
    for dimension in rect:
        print(dimension)
