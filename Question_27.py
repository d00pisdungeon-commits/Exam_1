import math

radius = int(input("Enter radius of circle: ")) #prompt user to enter radius as integer

area = math.pi * (radius ** 2) #use math module to calculate area
circumference = 2 * math.pi * (radius) #use math module to calculate circumference

print(f"Area of circle: {area}") #print area using F-string
print(f"Circumference of circle: {circumference}") #print circumference using F-stirng