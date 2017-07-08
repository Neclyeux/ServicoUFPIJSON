import json
from unidecode import unidecode

with open('/home/neclyeux/Documentos/UFPINews2/output.json') as file:
    data = json.load(file)
    for index in range(len(data)):
        lista = data[index]['news']
        for i in range(len(lista)):
            lista[i] = unidecode(lista[i])
        data[index]['news'] = lista

    with open('/home/neclyeux/Documentos/UFPINews2/saidaDecodificada.json', 'w') as outfile:
        json.dump(data, outfile)
