class Student:
    def __init__(self,rol,nam,mar):
        self.rol=rol
        self.nam=nam
        self.mar=mar

    def per(self):
        perc=(self.mar/900)*100
        return perc

    def rem(self):
        if self.per()<40.0:
            return "Fail"
        elif self.per()>=40.0:
            return "Pass"

    @staticmethod
    def idx(j=0):
        idn=j+1
        return idn

    def __repr__(self):
        return str(self.idx()) + str("                                   ") + str(self.nam) + str("                                   ") + str(self.rol) + str("                                  ") + str(self.mar) + str("                             ") + str(self.per()) + str("                          ") + str(self.rem())
