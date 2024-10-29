class Mangekant:
    def __init__(self,antallKanter:int,lengde_li:list):
        self.antallKanter = antallKanter
        self.lengde_li = lengde_li
    
    def angiLengder(self):
        for i in range(self.antallKanter):
            self.lengde_li.append(int(input(f"skriv lengde nummer {i}:")))
    
    def omkrets(self):
        self.o = sum(self.lengde_li)
    
    def visInfo(self):
        print(f"Mangekanten har {self.antallKanter} kanter, og har omkretsen {self.o}")

liste = []

a = Mangekant(5,[])
a.angiLengder()
liste.append(a)

b = Mangekant(5,[])
b.angiLengder()
liste.append(b)

c = Mangekant(5,[])
c.angiLengder()
liste.append(c)

