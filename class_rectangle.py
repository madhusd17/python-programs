class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
l=int(input("enter lenght of rectangle:"))
b=int(input("enter breadth of rectangle:"))
area_value=Rectangle(l,b)
print(f"Area of rectangle is {area_value.area()}")
