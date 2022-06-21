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

