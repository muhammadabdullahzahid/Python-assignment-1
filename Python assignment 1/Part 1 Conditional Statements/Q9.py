#9. Take three sides of a triangle as input and check if they form a valid triangle.
side1 = int (input ("Enter the 1st side of a triangle"))
side2 = int (input ("Enter the 2nd side of a trangle"))
side3 = int (input ("Enter the 3rd side of a triange"))
if side1 + side2 > side3 and side2 + side3 > side1 and side2 + side3 > side1:
    print ("The sides shows a valid trianle")
else:
    print ("The sides do not form a valid triangle ")