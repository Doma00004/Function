# def sum(a,b):
#     total=a+b
#     return total
# result=sum(6,9)
# print(result)

# def sum(*args):
#     total=args[0]+args[1]+args[2]
#     return total
# result=sum(6,9,5)
# print(result)


# #arbitary arguments-*args
# def sum(*args):
#     total=0
#     for n in args:
#         total+=n
#     return total
# result=sum(6,9,13,7,4)
# print(result)


#arbitary keyword argument
def hello(**kwargs):
    print("Hello",kwargs['name'],"Welcome to Web development Training")
    print(kwargs['course_name'])

hello(name="Ram",course_name="Python with django",another_course="Python with datascience")
