x="This is global variable"
def myfunc():
    x="This is local variable"
    print(x)
myfunc()
print(x)