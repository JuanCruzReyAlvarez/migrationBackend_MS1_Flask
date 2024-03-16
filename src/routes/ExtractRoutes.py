from flask import Blueprint, request, jsonify
from src.controller.ETLController import ETLController
import traceback

# Logger
from src.utils.Logger import Logger


main = Blueprint('extract_blueprint', __name__)


@main.route('/', methods=['POST'])
def extract():
    try:
            data = request.json
            message = ETLController.extractData(data)
            return message
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': "ERROR", 'success': False})
