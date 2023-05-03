

def import_data():
    # nombre_archivo = input("Ingrese el nombre del archivo a leer:")
    nombre_archivo = "data.csv"
    separador = ";"
    with open(nombre_archivo, encoding="utf-8") as archivo:
        next(archivo)
        
        datos = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            columnas = linea.split(separador)
            numero_region = int(columnas[0])
            region = columnas[1]
            provincia = columnas[2]
            circunscripcion_senatorial = int(columnas[3])
            distrito = int(columnas[4])
            comuna = columnas[5]
            circunscripcion_electoral = columnas[6]
            local = columnas[7]
            numero_mesa = int(columnas[8])
            tipo_de_mesa = columnas[9]
            mesas_fusionadas = columnas[10]
            electores = int(columnas[11])
            numero_en_voto = int(columnas[12])
            candidato = columnas[13]
            votos_tricel = int(columnas[14])
            
            datos.append({
                "numero de region": numero_region,
                "region": region,
                "provincia": provincia,
                "circunscripcion senatorial": circunscripcion_senatorial,
                "distrito": distrito,
                "comuna": comuna,
                "circunscripcion electoral": circunscripcion_electoral,
                "local": local,
                "numero de mesa": numero_mesa,
                "tipo de mesa": tipo_de_mesa,
                "mesas fusionadas": mesas_fusionadas,
                "electores": electores,
                "numero en voto": numero_en_voto,
                "candidato": candidato,
                "votos tricel": votos_tricel,
                })
        
        return datos   
       
def export_tables_by_region(data,filename):
    contador = 0
    mesas_regiones = []
    for numero_de_region in range(17):    
        
        for cont in range(len(data)):
            if data[cont]["numero de region"] == numero_de_region:
                contador +=1

        mesas_regiones.append(int(contador/4))
        contador = 0
    with open(filename,"w",encoding="utf-8") as file:
        file.write(f"DE TARAPACA {mesas_regiones[1]}\n")
        file.write(f"DE ATACAMA {mesas_regiones[2]}\n")
        file.write(f"DE COQUIMBO {mesas_regiones[3]}\n")
        file.write(f"DE VALPARAISO {mesas_regiones[4]}\n")
        file.write(f"DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS {mesas_regiones[5]}\n")
        file.write(f"DEL MAULE {mesas_regiones[6]}\n")
        file.write(f"DEL BIO BIO {mesas_regiones[7]}\n")
        file.write(f"DE LA ARAUCANIA {mesas_regiones[8]}\n")
        file.write(f"DE LOS LAGOS {mesas_regiones[9]}\n")
        file.write(f"DE AYSEN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO {mesas_regiones[10]}\n")
        file.write(f"DE MAGALLANES Y DE LA ANTARTICA CHILENA {mesas_regiones[11]}\n")
        file.write(f"METROPOLITANA DE SANTIAGO {mesas_regiones[12]}\n")
        file.write(f"DE LOS RIOS {mesas_regiones[13]}\n")
        file.write(f"DE ARICA Y PARINACOTA {mesas_regiones[14]}\n")
        file.write(f"DEL ÑUBLE {mesas_regiones[15]}\n")
        
        
    
def export_general_results(data, filename):
    candidatos = []
    votos = []
    for element in data:
        if element["candidato"] not in candidatos:
            candidatos.append(element["candidato"])
    
    for candidato in candidatos:
        contador = 0
        for element in data:
            if element["candidato"] == candidato:
                contador += element["votos tricel"]
        votos.append([candidato,contador])
        with open(filename,"w",encoding="utf-8") as file:
            for elemento in votos:
                file.write(f"{elemento[0]} {elemento[1]} \n")
        
                
            
                
def export_count_by_local(data, filename):
    local = input("INGRESE EL LOCAL QUE QUIERE ANALIZAR:")
    candidatos = []
    lista_ordenada = []
    for element in data:
        if element["candidato"] not in candidatos:
            candidatos.append(element["candidato"])
    for candidato in candidatos:
        contador = 0
        for element in data:
            if element["local"] == local and element["candidato"] == candidato:
                contador += element["votos tricel"]
        lista_ordenada.append([candidato,contador])
    with open(filename,"w",encoding = "utf-8") as archivo:
        for linea in lista_ordenada:
            archivo.write(linea[0])
            archivo.write(" ")
            archivo.write(str(linea[1]))
            archivo.write("\n")
            

datos = import_data()
export_tables_by_region(datos,"Mesas_por_region.csv")

export_general_results(datos, "Resultados_generales.csv")

export_count_by_local(datos, "Resultados_por_local_elegido.csv")








