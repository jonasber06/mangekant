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

class Rektangen(Mangekant):
    def __init__(self, antallKanter: int, lengde_li: list):
        super().__init__(antallKanter, lengde_li)
    
liste = []

a = Mangekant(5,[])
a.angiLengder()
liste.append(a)

b = Mangekant(7,[])
b.angiLengder()
liste.append(b)

c = Mangekant(3,[])
c.angiLengder()
liste.append(c)

for r in liste:
    r.omkrets()
    r.visInfo()

