def changeBat(fileDirectory, wordToFind, wordToChange, incremento):
    with open(fileDirectory,'r') as archivo:
        i=0
        j=0
        pos=[]
        for linea in archivo:
            linea=linea.lstrip()
            linea=linea.rstrip()
            if linea == wordToFind:
                print("match")
                pos.append(i)
                j=j+1
            i=i+1
        print("posicion del cambio = ", pos)

    contenido = open(fileDirectory).read().splitlines()
    for index in range(len(pos)):
        print(pos[index])
        contenido.insert(pos[index]-incremento,"            "+wordToChange)

    f = open('fileDirectory.yml', "w")
    f.writelines("\n".join(contenido))

changeBat("ola.txt","10.89.105.98","10.89.104.178",0)

