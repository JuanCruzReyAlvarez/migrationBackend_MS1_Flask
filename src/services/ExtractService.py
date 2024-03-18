
import base64
import csv
from io import StringIO

class ExtractService():
    @staticmethod
    def extractData(json):
        sortedListtableInfo = json.get('tables_info', [])
        files = ExtractService.listBase64ToCSV(json.get('files',[]))
        return (files, sortedListtableInfo )# Lista de archivos CSV 

    @staticmethod
    def listBase64ToCSV(listbase64):
        listFiles = list()
        for base64Element in listbase64:
            csv_file = ExtractService.base64ToCSV(base64Element)
            listFiles.append(csv_file)
        return listFiles

    @staticmethod
    def base64ToCSV(base64Element):
        base64Decode = base64.b64decode(base64Element)
        csv_text = base64Decode.decode('utf-8')
        csv_file = StringIO(csv_text)
        #reader = csv.reader(csv_file)
        # Se puede imprimir las filas para ver cómo se ven
        #for row in reader:
                #print(row)
        return csv_file


        