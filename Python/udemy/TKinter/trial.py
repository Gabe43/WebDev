# def add(*args):
#     z = 0
#     for n in args:
#         z = z+n
#     print(z)

# add(5,6,7,8,9,5)

def calculate(**kwargs):
    add = 0
    for item in kwargs['add']:
        add=add+item
    print(add)


calculate(add=[6,7,8,9,10])
