from flask import Blueprint, jsonify, request


JSON_MIME_TYPE = 'application/json'

sys_app = Blueprint('sys_app', __name__)

@sys_app.route('/', methods=['GET'])
def index():
	data = {
		'success': 'welcome to the test app',
		'status': 200
	}
	return jsonify(data)