#16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
a = int (input ("Enter a side of a triangle"))
b = int (input ("Enter b side of a traingle"))
c = int (input ("Enter c side of a triangle"))
if a == b ==c :
    print ("Triangle is equilateral")
elif a == b or a == c or b == c:
    print ("Triangle is isosceles")    
else:
    print ("traingle is scalene")    