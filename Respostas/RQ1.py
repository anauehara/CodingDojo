def right_justify(valor):
    s = str(valor)               
    space = (70 - len(s)) * '_'
    print(space + s)