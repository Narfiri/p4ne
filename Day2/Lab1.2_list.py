from openpyxl import load_workbook
from matplotlib import pyplot
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
def getvalue(x):
    return x.value
list_x = list(map(getvalue, sheet['A'][1:])) #years
print(list_x)

list_y = list(map(getvalue, sheet['C'][1:])) #temp
print(list_y)

list_z = list(map(getvalue, sheet['D'][1:])) #act
print(list_z)

print(sheet)
#print(type(sheet))
pyplot.plot(list_x, list_y, label="относительная температура к годам")
pyplot.plot(list_x, list_z, label="года к активности")
pyplot.show()


