while True:
    print("\n1.Area od circle\n2.Area of rectangle\n3.square\n4.triangle\n5.exit")
    choice=int(input("Enter choice between 1 to 5:"))
    if choice==1:
        r=float(input("enter radius"))
        print("Area of circle:",3.14*r*r)
    if choice==2:
        l=float(input("Enter length:"))
        b=float(input("Enter breath:"))
        print("Area of rectangle is:",l*b)
    if choice==3:
         s=float(input("Enter length:"))
         print("Area of Square is:",s*s)
    if choice==4:
        b=float(input("base:"))
        h=float(input("Height:"))
        print("Area of Triangle is:",0.5*h*b) 
    if choice==5:
        break
    else:
        print("Invalid choice")