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
l.insert(1,'hi')
print(l)
print(len(l)) #количество элементов в списке
from matplotlib import pyplot
from openpyxl import load_workbook
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
sheet['A'][1:]
def getvalue(x): return x.value
map(getvalue, sheet['A'][1:])
pyplot.plot(list_x, list_y, label="Метка")

def funk1 (x,y):
    return x+y
l1=[1,2,44,43]
l2=[4,5,76,12]
print (list(map(funk1,l1,l2)))
print(dir(fun))





