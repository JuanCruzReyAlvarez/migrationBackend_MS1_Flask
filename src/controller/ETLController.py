
from src.services.ExtractService import ExtractService
from src.services.TransformService import TransformService
from src.services.LoadService import LoadService
import json


class ETLController():

    @classmethod
    def extractData(data):

        ## 1° -> Extract
        data =  ExtractService.extractData(data) 
        files = data[0] 
        tablesInfo = data[1]
        ## 2° -> Transform
        ## filesTransformed = TransformService.transformData(files)  // -> No need in this project, it is prepared if it´s necessary 

        ## 3° -> Load

        LoadService.loadData(files, tablesInfo)  ## batch transactions (1 up to 1000 rows) with one request
        
    
        return "Base de datos Migrada"