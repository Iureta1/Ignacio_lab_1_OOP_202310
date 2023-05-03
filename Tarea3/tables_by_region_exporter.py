class TablesByRegionExporter:
    @classmethod
    def __init__(self,data,filename):
        self.filename = filename
        self.data = data


    @classmethod
    def export(self):
        
        contador = 0
        mesas_regiones = []
        for numero_de_region in range(17):    
            
            for cont in range(len(self.data)):
                if self.data[cont]["numero de region"] == numero_de_region:
                    contador +=1

            mesas_regiones.append(int(contador/4))
            contador = 0
        with open(self.filename,"w",encoding="utf-8") as file:
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
        