from flask import Blueprint, request, jsonify, make_response
from src.controller.ViewController import ViewController
import traceback
# Logger
from src.utils.Logger import Logger


main = Blueprint('view_blueprint', __name__)

@main.route('/viewEmployeesHiredDividedByQuarter', methods=['GET'])
def employeesHiredDividedByQuarter():
    try:
            return ViewController.viewEmployeesHiredWithRestriction()
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': "ERROR", 'success': False})


@main.route('/viewEmployeesHiredMoreThanMean', methods=['GET'])
def employeesHiredMoreThanMean():
    try:
            return ViewController.viewEmployeesIdNameNumberWithRestriction2021()
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': "ERROR", 'success': False})

