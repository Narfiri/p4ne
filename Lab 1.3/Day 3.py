def classify(i):...
i=1
while i <= 20:
    j=1
    while j <=20:
        print("%3d" % (i*j), end=" ")
        j = j + 1
    print("")
    i+=1

l=[1,2,10,15,12]
for x in l:
    print(x)

def sq(x):
    return x*x
for x in map(sq,l):
    print(x)

for i in range(1,21):
    for j in range(1, 21):
        print(i,j)

gen=(x*x for x in range (0,50))
print(type(gen))
for i in gen:
    print(i)

l=[x*x for x in range (0,50)]
print(l)

def fib(n): #циклы и фибоначчи
    a,b=1,1
    step=0
    while step<n:
        yield b
        b,a=a+b,b
        step+=1

for i in fib(100):
    print(i)

def fibr(n): #рекурсия для фибоначчи
    if n == 0 or n == 1:
        return 1
    else:
        return fibr(n - 1) +fibr(n - 2)
for i in range(100):
    print(fibr(i))
