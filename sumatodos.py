def sumaTodos(numeroSuperior):
    resultado = 0
    for i in range(0, numeroSuperior + 1):
        resultado += i
    
    return resultado


lista = [1,2,3,4,5,6,7,8,9,10]
listaDobles = map(lambda x: x*2, lista)
