#lambda function:the function without name. It is used for instant and one-time use. lambda keyword is used.
# x=lambda a,b:a+b
# sum=x(2,3)
# print(sum)

# y=lambda a,b:a*b
# mul=y(2,3)
# print(mul)

#recursive function - function calling itself again and again 
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(6))


