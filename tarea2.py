

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
       
def export_tables_by_region(data):
    contador = 0
    mesas_regiones = []
    for numero_de_region in range(17):    
        
        for cont in range(len(data)):
            if data[cont]["numero de region"] == numero_de_region:
                contador +=1

        mesas_regiones.append(int(contador/4))
        contador = 0
    print("DE TARAPACA",mesas_regiones[1],"\n",
          "DE ANTOFAGASTA", mesas_regiones[2],"\n",
          "DE ATACAMA", mesas_regiones[3],"\n",
          "DE COQUIMBO", mesas_regiones[4],"\n",
          "DE VALPARAISO", mesas_regiones[5],"\n",
          "DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS", mesas_regiones[6],"\n",
          "DEL MAULE", mesas_regiones[7],"\n",
          "DEL BIO BIO", mesas_regiones[8],"\n",
          "DE LA ARAUCANIA", mesas_regiones[9],"\n",
          "DE LOS LAGOS", mesas_regiones[10],"\n",
          "DE AYSEN DEL GENERAL CARLOS IBAÑEZ DEL CAMPO", mesas_regiones[11],"\n",
          "DE MAGALLANES Y DE LA ANTARTICA CHILENA", mesas_regiones[12],"\n",
          "METROPOLITANA DE SANTIAGO", mesas_regiones[13],"\n",
          "DE LOS RIOS", mesas_regiones[14],"\n",
          "DE ARICA Y PARINACOTA", mesas_regiones[15],"\n",
          "DEL ÑUBLE", mesas_regiones[16],"\n",
          )
    


datos = import_data()
mesas_por_region = export_tables_by_region(datos)

# export_tables_by_region(datos, mesas_por_region)










