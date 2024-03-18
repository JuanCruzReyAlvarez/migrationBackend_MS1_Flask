from flask import Blueprint, request, jsonify, make_response
from src.controller.ETLController import ETLController
import traceback

# Logger
from src.utils.Logger import Logger


main = Blueprint('extract_blueprint', __name__)


@main.route('/extract', methods=['POST'])
def extract():
    try:
            data = request.get_json()
            return ETLController.extractData(data)
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': "ERROR", 'success': False})
