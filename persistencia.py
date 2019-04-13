"""
Calcular la persistencia multiplicativa de este número es muy sencillo. Todo lo que requiere es
multiplicar sus dígitos, tomar el resultado, y repetir el proceso hasta que ya no sea posible.
Veamos: 7x7x9x3=1323, 1x3x2x3=18, 1×8=8. La persistencia multiplicativa de 7793 es de apenas 3 pasos.

El número conocido más alto es 277777788888899 con 11 pasos
"""

def per(n, nVez=0):
    if len(str(n))==1:
        #print(n)
        return "Done"
    
    digits = [int(i) for i in str(n)]
    nVez += 1
    
    result = 1
    for j in digits:
        result *= j
    print(nVez, result)
    per(result, nVez)

# 277777788888899 -> 11