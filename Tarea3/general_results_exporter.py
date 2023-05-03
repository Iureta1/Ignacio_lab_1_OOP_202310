class GeneralResultsExporter:

    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def export(self):

        candidatos = []
        votos = []
        for element in self.data:
            if element["candidato"] not in candidatos:
                candidatos.append(element["candidato"])
        
        for candidato in candidatos:
            contador = 0
            for element in self.data:
                if element["candidato"] == candidato:
                    contador += element["votos tricel"]
            votos.append([candidato,contador])
            with open(self.filename,"w",encoding="utf-8") as file:
                for elemento in votos:
                    file.write(f"{elemento[0]} {elemento[1]} \n")       
            


