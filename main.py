import numpy
# funcion para convetir la columna a entero
def ColToInt(dataset, index):
    for register in dataset:
        if len(register[index]) == 0:
            register[index] = 0
        else:
            register[index] = int(register[index])

# funcion para convertir la columna a flotante
def ColToFloat(dataset, index):
    for register in dataset:
        if len(register[index]) == 0:
            register[index] = 0
        else:
            register[index] = float(register[index])

# funcion para normalizar los datos
def Normalizar(dataset, index):
    cols = list(zip(*dataset))
    maximo = max(cols[index])
    minimo = min(cols[index])
    for row in dataset:
        # norm = 5*(x-min)/(max-min)
        row[index] = round(5*(row[index]-minimo)/(maximo-minimo), 2)

# funcion para estandarizar los datos
def Estandarizacion(dataset, index):
    cols = list(zip(*dataset))
    xPrima = numpy.average(cols[index])
    sigma = numpy.std(cols[index])
    for row in dataset:
        row[index] = round((row[index] - xPrima) / sigma, 2)

# funcion para eliminar una columna
def DelColumn(dataset, cabecera, index):
    del(cabecera[index])
    for row in dataset:
        del(row[index])

if __name__ == "__main__":
    # modificacion del datset
    cabecera = []
    dataset = []
    archivo = open("heart_failure_clinical_records_dataset.csv", "r")
    for linea in archivo:
        linea = linea.strip().split(",")
        dataset.append(linea)
    archivo.close()
    cabecera = dataset.pop(0)

    enteros = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12]
    flotantes = [0, 6, 7]
    for integer in enteros:
        ColToInt(dataset, integer)

    for decimal in flotantes:
        ColToFloat(dataset, decimal)

    # la normalizacion se ocoupa para datos lejanos (rango)
    # la estandarizacion se ocupa para datos no muy lejanos (que tan alejados estan de la media)
    # normalizamos o estandarizamos dependiendo de como se comporten los datos
    Normalizar(dataset, 0)
    Normalizar(dataset,2)
    Estandarizacion(dataset, 4)
    Normalizar(dataset,6)
    Estandarizacion(dataset,8)
    Normalizar(dataset,11)

    print(cabecera)
    for row in dataset:
        print(row)

    # escribimos el dataset modificado en un archivo nuevo
    archivo = open("HeartFailureOut.csv", "w")
    archivo.write(",".join(cabecera))
    archivo.write("\n")
    for row in dataset:
        for i in range(len(row)):
            row[i] = str(row[i])
        archivo.write(",".join(row))
        archivo.write("\n")
    archivo.close()