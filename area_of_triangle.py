import math
a = float(input())
b = float(input())
c = float(input())
if a+b>c or b+c>a or a+c>b:
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))
    if area < 0:
        print("Invalid Triangle")
    else:    
        print("The area of the triangle is: {:.2f}".format(math.sqrt(area)))

