class a1:
    def __init__(self, x):
        self.x=x
    
class a2(a1):
    def __init__(self, x, y):
        a1.__init__(self, x)
        self.y=y

class a3(a2):
    def __init__(self, x, y, z):
        a2.__init__(self, x, y)
        self.z=z
        

p=a3(5, 2, 4)
print(p.x, p.y, p.z)
