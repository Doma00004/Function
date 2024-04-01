#Function is a block of code.We use function to reuse the code. There are two types of function: Build-in function and User defined function.
# def function_name():
#     function body
# function_name()

#simple program in user defined function.
# def name():
#     print("Hello World")
# name()


# n=input("Enter your name")
# a=input("Enter your course name")
# def name(n, a): #parameter
#     print("Hello",n,"Welcome to Web development Training")
#     print(a)
# name(n,a)  #argument


#positional arguments:takes value according to proper positional order
def hello(name, course_name):
    print("Hello",name,"Welcome to Web development Training")
    print(course_name)

hello("Ram","Python with django")


#keyword arguments:takes value according to keyword
def hello(name, course_name):
    print("Hello",name,"Welcome to Web development Training")
    print(course_name)

hello(course_name="Python with django",name="Ram")  


#default arguments
def hello(name, course_name="Python with django"):
    print("Hello",name,"Welcome to Web development Training")
    print(course_name)

hello(name="Ram")  

def hello(name, course_name="Python with django"):
    print("Hello",name,"Welcome to Web development Training")
    print(course_name)

hello(name="Ram",course_name="Python with Data Science")  


