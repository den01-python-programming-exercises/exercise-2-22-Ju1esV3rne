class Example(object):
    """docstring fo Example."""

    def __init__(self, *args):
        self.print_text()

    def print_text(self):
        print("In a hole in the ground there lived a method")


def main():
    #write your code below this line
    num = int(input("How many times?"))
    for i in range(num):
        x = Example()

if __name__ == '__main__':
    main()
