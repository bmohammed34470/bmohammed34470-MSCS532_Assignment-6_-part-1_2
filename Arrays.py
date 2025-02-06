class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
    
    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def delete(self, index):
        if 0 <= index < self.size:
            self.array[index] = None
        else:
            raise IndexError("Index out of bounds")

    def access(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        return self.array

# Usage
arr = Array(int(input("Enter the size of array : ")))
print("Choose the below options : ")
print("1. Insert Element\n2. Delete Element\n3. Access Element\n4. Display array")
a = True
while a == True:
    x = int(input("Enter your Option : "))
    if x == 1:
        arr.insert(int(input("Enter the index value to be inserted in : ")), int(input("Enter the Element : ")))
    elif x == 2:
        arr.delete(int(input("Enter the index value to be deleted : ")))
    elif x == 3:
        print(arr.access(int(input("Enter the index value to be Accessed : "))))
    elif x == 4:
        print(arr.display())
    else:
        a = False
        
