class Subnet:
    def __init__(self, n="0.0.0.0", p="/0"):
        self.network = n
        self.prefix = p
    def __str__(self): # метод для преобразования результата в строку
        return self.network + self.prefix
    def __repr__(self): # метод для отображения объекта в интерактивном режиме
        return self.network + self.prefix
    def getnet(self):
        return self.network
    def getprefix(self):
        return self.prefix
n1 = Subnet("192.168.1.0", "/24")
n2 = Subnet("172.16.0.0", "/16")

print(type(n1))
print(n1)
print(n1.getprefix())
print(n1.prefix)
print(Subnet.getnet(n1))
print(n1.getnet())
print("_________")

class Addr_plan_entry(Subnet):
    def __init__(self, n="0.0.0.0", p="/0", gw="0.0.0.0"):
        Subnet.__init__(self, n, p)
        self.gateway = gw
    def getgw(self):
        return self.gateway

a1 = Addr_plan_entry("192.168.1.0", "/24", "192.168.1.1")
print(a1)
print(a1.getgw())
print(dir(a1)) #справка об a1
print(Addr_plan_entry.__bases__) #посмотреть от какого класса данный класс унаследован




