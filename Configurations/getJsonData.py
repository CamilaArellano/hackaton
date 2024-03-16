#@Angel Pinacho

#recuperar datos del Json
import json

class getJsonData():
    def __init__(self):
        self.data_list = []

    def getJsonData(self, ruta):

        with open(ruta) as contenido:
            datos = json.load(contenido)

            casos = datos.get("cases", [])  # Obtiene la lista de casos
            for caso in casos:
                _row=[] 
                case_id = caso.get("case_id")  # Obtiene el case_id del caso
                distribution = caso.get("distribution")  # Obtiene la distribution del caso
                _row.append(case_id) 
                _row.append(distribution)
        
                sub_casos = caso.get("sub_cases", [])  # Obtiene la lista de subcasos
                for sub_caso in sub_casos:
                    _row2=[] 
                    case_id = sub_caso.get("case_id")  # Obtiene el case_id del subcaso
                    distribution = sub_caso.get("distribution")  # Obtiene la distribution del subcaso
            
                    _row2.append(case_id)
                    _row2.append(distribution)

                    _row.append(_row2)
                self.data_list.append(_row)

    def getPerArc(self, ruta):
        with open(ruta) as contenido:
            datos = json.load(contenido)
            records_per_arc = datos.get("records_per_arc")
            return records_per_arc


    def getSimilarData(self):
        listSimilar = self.data_list[0]
        listSimilarData = []
        cont = 0

        for item in listSimilar:
            if cont <= 1:
                listSimilarData.append(item)
            cont = cont + 1
        for item in listSimilar[2]:
            listSimilarData.append(item)
        for item in listSimilar[3]:
            listSimilarData.append(item)

        return listSimilarData
    

    def getFamilyData(self):
        listFamily = self.data_list[1]
        listFamilyData = []
        cont = 0
        for item in listFamily:
            if cont <= 1:
                listFamilyData.append(item)
            cont = cont + 1
        for item in listFamily[2]:
            listFamilyData.append(item)
        for item in listFamily[3]:
            listFamilyData.append(item)
        for item in listFamily[4]:
            listFamilyData.append(item)

        return listFamilyData
    
    def getLowSimilitary(self):
        listLowSimilitary = self.data_list[2]
        listLowSimilitaryData = []
        cont = 0
        for item in listLowSimilitary:
            if cont <= 1:
                listLowSimilitaryData.append(item)
            cont = cont + 1
        for item in listLowSimilitary[2]:
            listLowSimilitaryData.append(item)
        for item in listLowSimilitary[3]:
            listLowSimilitaryData.append(item)
        for item in listLowSimilitary[4]:
            listLowSimilitaryData.append(item)
        for item in listLowSimilitary[5]:
            listLowSimilitaryData.append(item)

        return listLowSimilitaryData


ruta='config_file.json'

obj = getJsonData()
obj.getJsonData(ruta)

listSimilar = obj.getSimilarData()
listFamily = obj.getFamilyData()
listLowSimilitary = obj.getLowSimilitary()
PerArc= obj.getPerArc(ruta)

 
print(PerArc)
        
