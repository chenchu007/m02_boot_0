class Perro():
    def __init__(self,nombre,edad=0,peso=0):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self, mensaje=""):
        print("{}: Guau, guau. {}".format(self.nombre, mensaje), end="")

    def __str__(self):
        return "Soy un perro llamado {}".format(self.nombre)

class PerroAsistencia(Perro):
    def __init__(self,nombre,edad=0,peso=0,amo="mi dueño"):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self._trabajando = False

    def __str__(self):
        return("Soy el perro de asistencia de {}".format(self.amo))

    def ladrar(self):
        if self.__trabajando:
            print("{}: shhh, estoy trabajando".format(self.nombre))
        else:
            Perro.ladrar(self)

    def trabajando(self,valor=None):
            if valor == None:
                return self.__trabajando
            else:
                self.__trabajando = valor
