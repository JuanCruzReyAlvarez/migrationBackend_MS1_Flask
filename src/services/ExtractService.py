
class ExtractService():
    @classmethod
    def extractData(request):
        return (request.files.getlist('files'), request.json.get('tables_info', []) )# Lista de archivos CSV 
        