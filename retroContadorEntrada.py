def retroContadorEntrada(e):
    print(str(e) + ',', end="")
    if e>1:
        retroContadorEntrada(e-1)
    else:
        print("0")
    return

retroContadorEntrada(10)