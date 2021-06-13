def s(a,b,c):
    print(str(a+b+c))

def f(l, *args):
    l(*args)

f(s, 1, 2, 4)