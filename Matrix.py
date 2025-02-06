class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[None] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
        else:
            raise IndexError("Index out of bounds")

    def delete(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = None
        else:
            raise IndexError("Index out of bounds")

    def access(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.matrix[row][col]
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        return self.matrix

# Usage
arr = Matrix(int(input("Enter the no. of rows : ")), int(input("Enter the no. of Coloumns : ")))
print("Choose the below options : ")
print("1. Insert Element\n2. Delete Element\n3. Access Element\n4. Display array")
a = True
while a == True:
    x = int(input("Enter your Option : "))
    if x == 1:
        arr.insert(int(input("Enter the rows no. : ")), int(input("Enter the Coloumn no. : ")), int(input("Enter the Element : ")))
    elif x == 2:
        arr.delete(int(input("Enter the rows no. : ")), int(input("Enter the Coloumn no. : ")))
    elif x == 3:
        print(arr.access(int(input("Enter the rows no. : ")), int(input("Enter the Coloumn no. : "))))
    elif x == 4:
        print(arr.display())
    else:
        a = False