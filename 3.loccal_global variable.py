l=float(input("Enter length:"))
b=float(input("Enter breadth:"))
def area():
    global re   #global variable can be accessible from anywhere
    re=l*b
    return re
result=area()
print(result)

#local variable:defined inside the function and is not accessible from outside the function
def volume():
    h=float(input("Enter height:"))
    v=re*h
    return v
vol=volume()
print(vol)


#self
l=float(input("Enter length:"))
b=float(input("Enter breadth:"))
def area():
    re=l*b
    return re
a=area()
print("Area:",a)

def volume():
    h=float(input("Enter height:"))
    v=area()*h
    return v
vol=volume()
print("Volume:",vol)