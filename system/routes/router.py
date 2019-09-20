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

@sys_app.route('/add', methods=['GET','POST'])
def add_nums():
	if request.method == 'POST':
		if request.content_type != JSON_MIME_TYPE:
			return jsonify({'status': 406, 'error': 'Invalid data content type - use JSON'}), 406

		data = request.get_json()
		x = data['num1'] + data['num2']
		
		return jsonify({"total":x}), 202
	else:
		data = {
			'info': 'add two numbers',
			'status': 202
		}
		return jsonify(data), 202


