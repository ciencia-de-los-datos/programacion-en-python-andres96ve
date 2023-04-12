"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    archivo=open(".\data.csv")
    datos=[]
    suma=0
    for i in range(40):
            lectura=archivo.readline().split("\t")
            datos.append(lectura)

    for n in range(len(datos)):
            suma += int(datos[n][1])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    archivo=open(".\data.csv")
    datos=[]
    datos_primeracol=[]
    datos_no_repetido=[]
    numeros_veces=[]
    tuplas=()
    lista_tuplas=[]
    for i in range(40):
            lectura=archivo.readline().split("\t")
            datos.append(lectura)
    for n in range(len(datos)):
            datos_primeracol.append(datos[n][0])

    for dato in datos_primeracol:
            if dato not in datos_no_repetido:
                    datos_no_repetido.append(dato)
    datos_no_repetido.sort()
    for letra in datos_no_repetido:
            numeros_veces.append(datos_primeracol.count(letra))


    for a in range(len(datos_no_repetido)):
            lista_tuplas.append((datos_no_repetido[a],numeros_veces[a]))
            
    return lista_tuplas 


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    archivo=open(".\data.csv")
    [suma0,suma1,suma2,suma3,suma4]=[0,0,0,0,0]
    sumas=[]
    datos=[]
    datos_primeracol=[]
    datos_segundacol=[]
    datos_no_repetido=[]
    lista_tuplas=[]
    for i in range(40):
            lectura=archivo.readline().split("\t")
            datos.append(lectura)
    for n in range(len(datos)):
            datos_primeracol.append(datos[n][0])
    for k in range(len(datos)):
            datos_segundacol.append(datos[k][1])


    for dato in datos_primeracol:
            if dato not in datos_no_repetido:
                    datos_no_repetido.append(dato)
    datos_no_repetido.sort()

    for p in range(len(datos_primeracol)):
            if datos_primeracol[p]==datos_no_repetido[0]:
                    suma0 +=int(datos_segundacol[p])
            elif datos_primeracol[p]==datos_no_repetido[1]:
                    suma1 +=int(datos_segundacol[p])
            elif datos_primeracol[p]==datos_no_repetido[2]:
                    suma2 +=int(datos_segundacol[p])
            elif datos_primeracol[p]==datos_no_repetido[3]:
                    suma3 +=int(datos_segundacol[p])
            elif datos_primeracol[p]==datos_no_repetido[4]:
                    suma4 +=int(datos_segundacol[p])
    sumas +=suma0,suma1,suma2,suma3,suma4
    for q in range(len(sumas)):
            lista_tuplas.append((datos_no_repetido[q],sumas[q]))
    return lista_tuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    archivo=open(".\data.csv")
    meses=[]
    sumas=[0,0,0,0,0,0,0,0,0,0,0,0]
    datos=[]
    datos_terceracol=[]
    lista_tuplas=[]
    nuevos_datos=[]
    for i in range(40):
            lectura=archivo.readline().split("\t")
            datos.append(lectura)
    for n in range(len(datos)):
            datos_terceracol.append(datos[n][2])

    for j in range(len(datos_terceracol)):
            nuevos_datos.append(datos_terceracol[j].split("-"))
    for dato in nuevos_datos:
            if dato[1] not in meses:
                    meses.append(dato[1])
    meses.sort()

    for u in range(len(meses)):
            for t in range(len(datos_terceracol)):
                    if meses[u] in nuevos_datos[t][1]:
                            sumas[u] +=1
    for q in range(len(sumas)):
            lista_tuplas.append((meses[q],sumas[q]))
    return lista_tuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    archivo=open(".\data.csv")

    data=[]
    datos=[]
    datos_mayores=[0,0,0,0,0]
    datos_menores=[0,0,0,0,0]
    datos_primeracol=[]
    datos_segundacol=[]
    datos_no_repetido=[]
    lista_tuplas=[]
    for i in range(40):
            lectura=archivo.readline().split("\t")
            datos.append(lectura)
    for n in range(len(datos)):
            datos_primeracol.append(datos[n][0])

    for k in range(len(datos)):
            datos_segundacol.append(datos[k][1])


    dato_mayor=datos_segundacol[0]
    dato_menor=datos_segundacol[0]
    for dato in datos_primeracol:
            if dato not in datos_no_repetido:
                    datos_no_repetido.append(dato)
    datos_no_repetido.sort()

    for p in range(len(datos_no_repetido)): 
            dato_mayor=0
            for n in range(len(datos_primeracol)):   
                    if datos_primeracol[n]==datos_no_repetido[p] and int(datos_segundacol[n])>int(dato_mayor):
                                    dato_mayor=datos_segundacol[n]
                                    datos_mayores[p]=dato_mayor
                                    
    for q in range(len(datos_no_repetido)): 
            dato_menor=datos_mayores[q]        
            for o in range(len(datos_primeracol)):   
                    
                    if datos_primeracol[o]==datos_no_repetido[q] and int(datos_segundacol[o])<int(dato_menor):
                                    dato_menor=datos_segundacol[o]
                                    datos_menores[q]=dato_menor
    for r in range(len(datos_no_repetido)):
            lista_tuplas.append((datos_no_repetido[r],int(datos_mayores[r]),int(datos_menores[r])))


    return lista_tuplas


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open(".\data.csv") as archivo:
      
        datos=[]
        datos_cuartacol=[]
        nuevos_datos=[]
        diccionario={}
        
        lista_tuplas=[]

        archivo=[linea.replace("\n","") for linea in archivo]
        archivo=[linea.split("\t") for linea in archivo]
        datos=archivo
        
        for n in range(len(datos)):
                datos_cuartacol.append(datos[n][4])

        for j in range(len(datos_cuartacol)):
                nuevos_datos.append(datos_cuartacol[j].split(","))

        for dato in nuevos_datos:
                for cada in dato:
                        clave,valor=cada.split(":")
                        if clave not in diccionario:
                                diccionario[clave] = [int(valor)]
                        else:
                                diccionario[clave].append(int(valor))
        for clave in diccionario:
                valores=diccionario[clave]
                maximo_dato=max(valores)
                minimo_dato=min(valores)
                lista_tuplas.append((clave,minimo_dato,maximo_dato))
                
        lista_tuplas.sort()

    return lista_tuplas


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open(".\data.csv") as datos:
        datos=[n.split("\t") for n in datos]
        datos_primeracol=[n[0] for n in datos]
        datos_segundacol=[n[1] for n in datos]
        lista=[]
        numeros=[]
        letra=[]
        lista_tuplas=[]
        for dato in datos_segundacol:
                if dato not in numeros:
                        numeros.append(dato)
        
        numeros.sort()
        for m in range(len(numeros)):
                lista=[]
                for numero,letras in zip(datos_segundacol,datos_primeracol):
                        pares=numero,letras

                        if pares[0]==numeros[m]:
                                lista.append(pares[1])
                                       
                letra.append(lista)
        for o in range(len(numeros)):

                lista_tuplas.append((int(numeros[o]),letra[o]))
    return lista_tuplas


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open(".\data.csv") as datos:
        datos=[n.split("\t") for n in datos]
        datos_primeracol=[n[0] for n in datos]
        datos_segundacol=[n[1] for n in datos]
        lista=[]
        numeros=[]
        letra=[]
        lista_tuplas=[]
        for dato in datos_segundacol:
                if dato not in numeros:
                        numeros.append(dato)
        
        numeros.sort()
        for m in range(len(numeros)):
                lista=[]
                for numero,letras in zip(datos_segundacol,datos_primeracol):
                        pares=numero,letras

                        if pares[0]==numeros[m] and pares[1] not in lista:
                                lista.append(pares[1])
                                lista.sort()
                                       
                letra.append(lista)
        for o in range(len(numeros)):

                lista_tuplas.append((int(numeros[o]),letra[o]))
    return lista_tuplas


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open(".\data.csv") as archivo:
      
        datos=[]
        datos_cuartacol=[]
        nuevos_datos=[]
        diccionario={}
        diccionario2={}
        diccionario2_ord={}
        
        lista_tuplas=[]

        archivo=[linea.replace("\n","") for linea in archivo]
        archivo=[linea.split("\t") for linea in archivo]
        datos=archivo
        
        for n in range(len(datos)):
                datos_cuartacol.append(datos[n][4])

        for j in range(len(datos_cuartacol)):
                nuevos_datos.append(datos_cuartacol[j].split(","))

        
        for dato in nuevos_datos:
                
                for cada in dato:
                        clave,valor=cada.split(":")
                        if clave not in diccionario:
                                diccionario[clave] = [int(valor)]
                        else:
                                diccionario[clave].append(int(valor))
        
        for clave in diccionario:
                
                valores=diccionario[clave]
                
                cant=len(valores)
                diccionario2[clave]=len(valores)
                
        lista_ord_diccionario2=sorted(diccionario2.items())
        
        for key, value in lista_ord_diccionario2:
                diccionario2_ord[key]=value

    return diccionario2_ord


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open(".\data.csv") as datos:
        datos=[n.split("\t") for n in datos]
        datos_primeracol=[n[0] for n in datos]
        datos_cuartacol=[n[3] for n in datos]
        datos_quintacol=[n[4] for n in datos]
        lista_cant_cuartacol=[]
        lista_cant_quintacol=[]
        lista_tuplas=[]

        for dato in datos_cuartacol:
                lista_cant_cuartacol.append(len(dato.split(",")))
        
        for date in datos_quintacol:
                lista_cant_quintacol.append(len(date.split(",")))
        
        for o in range(len(datos_primeracol)):
                lista_tuplas.append((datos_primeracol[o],lista_cant_cuartacol[o],lista_cant_quintacol[o]))

    return lista_tuplas


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open(".\data.csv") as datos:
        datos=[n.split("\t") for n in datos]
        datos_segundacol=[n[1] for n in datos]
        datos_cuartacol=[n[3] for n in datos]
        datos_cuartacol=[n.split(",") for n in datos_cuartacol]
        letras=[]
        numeros=[]
        numeros_final=[]
        diccionario={}
        

        for dato in datos_cuartacol:
                for letra in dato:
                        if letra not in letras:
                                letras.append(letra)
        letras.sort()
        for m in range(len(letras)):
                lista=[]
                for p in range(len(datos_cuartacol)):
                        if letras[m] in datos_cuartacol[p]:
                                lista.append(int(datos_segundacol[p]))
                numeros.append(lista)
        
        for sublista in numeros:
                numeros_final.append(sum(sublista))

        diccionario=dict(zip(letras,numeros_final))
    return diccionario


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open(".\data.csv") as datos:
        datos=[linea.replace("\n","") for linea in datos]
        datos=[linea.split("\t") for linea in datos]
        
        datos_primeracol=[n[0] for n in datos]
        datos_quintacol=[n[4] for n in datos]
        datos_quintacol=[n.split(",") for n in datos_quintacol]
        letras=[]
        lista2=[]
        lista3=[]
        diccionario={}
        diccionario_final={}

        for dato in datos_primeracol:
                if dato not in letras:
                        letras.append(dato)
        
        
        for dato in datos_quintacol:      
                diccionario={}
                for cada in dato:       
                        clave,valor=cada.split(":")
                        if clave not in diccionario:
                                diccionario[clave] = int(valor)
                        else:
                                diccionario[clave].append(int(valor))
                lista=list(diccionario.values())
                lista2.append(sum(lista))
       
               
        for m in range(len(letras)):
                lis=[]
                for letra,numeros in zip(datos_primeracol,lista2):

                        if letra==letras[m]:
                                lis.append(int(numeros))                         
                lista3.append(sum(lis))
        
        diccionario_final_desord=dict(zip(letras,lista3))

        lista_diccionario_final=sorted(diccionario_final_desord.items())
        
        for key, value in lista_diccionario_final :
                diccionario_final[key]=value

    return diccionario_final 