# Encapsulation


class myClass(object):
    def __init__(self):
        self.a = 123  
        self._b = 123  
        self.__c = 123  

obj = myClass()
print(obj.a)  
print(obj._b)  
print(obj.__c)  


class myClass(object):
    def __init__(self):
        self.__version = 22  

    def getVersion(self):
        print(self.__version)

    def setVersion(self, version):
        self.__version = version

obj = myClass()
obj.getVersion()  
obj.setVersion(23)
obj.getVersion()  


print(obj._myClass__version)  # This will print 23

