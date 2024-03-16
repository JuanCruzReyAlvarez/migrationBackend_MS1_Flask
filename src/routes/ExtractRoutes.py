from flask import Blueprint, request, jsonify

import traceback

# Logger
from src.utils.Logger import Logger

# Security
from src.utils.Security import Security


main = Blueprint('extract_blueprint', __name__)


@main.route('/', methods=['POST'])
def extract():
    try:
            return None
    except Exception as ex:
        Logger.add_to_log("error", str(ex))

        return jsonify({'message': "ERROR", 'success': False})
