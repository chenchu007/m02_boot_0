class temperatura():
    def __init__(self,temperatura=0,unidad="C"):
        self.temperatura = temperatura
        self.unidMedida = unidad.upper()

    def mide(self, unidLectura="C"):
        unidConversion = unidLectura.upper()
        if unidConversion == "C" or unidConversion == "F" or unidConversion == "K":
            if unidConversion != self.unidMedida:
                if unidConversion == "C":
                    if self.unidMedida == "F":
                        self.temperatura = (self.temperatura - 32) * (5/9)
                    else:
                        self.temperatura -= 273.15
                elif unidConversion == "F":
                    if self.unidMedida == "C":
                        self.temperatura = self.temperatura * (9/5) + 32
                    else:
                        self.temperatura = (self.temperatura - 273.15) * 9/5 + 32
                else:
                    if self.unidMedida == "F":
                        self.temperatura = (self.temperatura - 32) * 5/9 + 273.15
                    else:
                        self.temperatura += 273.15
                self.unidMedida = unidLectura
            self.unidMedida = unidConversion
        return self.__str__()

    def __str__(self):
        return "{:.2f}º {}".format(self.temperatura,self.unidMedida)
                
if __name__ == "__main__":
    t1=temperatura()
    print(t1.mide("F"))
    print(t1.mide("K"))
    print(t1.mide("F"))
