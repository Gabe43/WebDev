# class User:
#     def __init__(self,name) -> None:
#         self.name = name
#         self.is_logged_in = False
    
# def is_authenticated_decorator(function):
#     def wrapper(*args,**kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper

# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")


# txt = User('angela')
# txt.is_logged_in = True
# create_blog_post(txt)




# def logging_decorator(func):
#     def wrapper(*args):
#         print(f'You called {func.__name__}{args}')
#         func(args[0],args[1],args[2])
#     return wrapper

# @logging_decorator
# def a_function(a,b,c):
#     name = 'a_function'
#     d = a+b+c
#     print (f'It returned:  {d}')


# a_function(1,2,3)
