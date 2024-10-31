print("")
class Mangekant:
    """klasse for kor mykje sidar ein figur har med kor lang kvær sida er"""
    def __init__(self,antallKanter:int,lengde_li:list):
        self.antallKanter = antallKanter
        self.lengde_li = lengde_li
    
    def angiLengder(self):
        """du kan sette in lengdene til figuren med denne funksjona"""
        print("")
        for i in range(self.antallKanter):
            self.lengde_li.append(int(input(f"skriv lengde nummer {i+1}/{self.antallKanter}: ")))
    
    def omkrets(self):
        """denne funksjonan finna omkretsa tel ein figur"""
        self.o = sum(self.lengde_li)
    
    def visInfo(self):
        """viser infoen til figura"""
        print(f"Mangekanten har {self.antallKanter} kanter, og har omkretsen {self.o}")

class Rektangel(Mangekant):
    def __init__(self, lengde_li: list):
        super().__init__(4,lengde_li)
    
    def angiLengder(self):
        for i in range(2):
            if i ==0:
                self.a = int(input(f"skriv lengde: "))
                self.lengde_li.append(self.a)
                self.lengde_li.append(self.a)

            if i != 0:
                self.a = int(input(f"skriv bredde: "))
                self.lengde_li.append(self.a)
                self.lengde_li.append(self.a)

    
liste = []

""" a = Mangekant(5,[])
a.angiLengder()
liste.append(a)

b = Mangekant(7,[])
b.angiLengder()
liste.append(b)

c = Mangekant(3,[])
c.angiLengder()
liste.append(c) """

d = Rektangel([])
d.angiLengder()
liste.append(d)

for r in liste:
    r.omkrets()
    r.visInfo()

