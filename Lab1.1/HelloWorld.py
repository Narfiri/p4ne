import sys

print("Hello,world")
s='my text'
print(s)
print(sys.getsizeof(s))
s='another text'
print(sys.getsizeof(s))
print(s[2:5])
def test(x):
    print(x)
    return x*x
print (test(50)+test(20))
print(8/5)
print(8//5)
print(8%5) #остаток после целого деления
print(dir(s))
l=[2,3,10,50]
print(type(l))
print(l[3])
print(l.index(50))
l.remove(50)
print(l)
del l[1]
print(l)


