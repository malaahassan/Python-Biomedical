class Point2D: #Defines a class called Point2D
    def __init__(self, x=0, y=0): #Defines the constructor with x, y having default values of 0
        self.x = x #sets the x property of this instance equal to x from the constructor parameter
        self.y = y #sets the y property of this instance equal to y from the constructor parameter

    def __str__(self): #Defines __str__ function which controls how the object is represented as a string
        return f"({self.x}, {self.y})" #Returns this string when object is printed

    def add(self, p): #Defines a method to add another point p to the current one
        self.x += p.x #This line adds the x propery of object p to x property of this instance
        self.y += p.y #This line adds the y propery of object p to y property of this instance

    def distance(self, p): #Defines a method to calculate the distance between this point and point p
        delta_x = self.x - p.x #This line subtracts the x property of p from this instance's x property and saves it variable delta_x
        delta_y = self.y - p.y #This line subtracts the y property of p from this instance's y property and saves it variable delta_y

        dist = (delta_x ** 2 + delta_y ** 2) ** 0.5 #This line calculates the distance using the variables delta_x, delta_y and saves the result in variable dist
        return dist #returns the value of variable dist


p1 = Point2D(1, 2)
p2 = Point2D(4, -2)

p2.add(p1)

print(p2)
print(p1.distance(p2))