from flask import Blueprint, jsonify, request, abort


JSON_MIME_TYPE = 'application/json'

sys_app = Blueprint('sys_app', __name__)


@sys_app.route('/', methods=['GET'])
def index():
	data = {
		'success': 'welcome to the test app v1',
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


@sys_app.route('/form/add',methods=['POST','GET'])
def form_add():
	if request.method == 'POST':
		num1 = int(request.form['num1'])
		num2 = int(request.form['num2'])
		return '''{} + {} = {}'''.format(num1,num2,(num1+num2))

	return '''
	<!doctype html>
	<html>
		<head>
			<title>My Good App!</title>
		</head>
		<body>
			<form method="POST">
				<input type="number" name="num1" placeholder="First number!"  style="min-width:150px;"><br>
				<input type="number" name="num2" placeholder="Second number!" style="min-width:150px;"><br>
				<input type="submit" value="ADD">
			</form>
		</body>
	</html>
	'''


@sys_app.route('/data/inputs',methods=['POST','GET'])
def input_data():
	if request.method == 'POST':
		data = request.get_json()
	abort(403)

