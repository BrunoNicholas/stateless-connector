from flask import Flask, jsonify

from .routes.router import sys_app

app = Flask(__name__)

# capturing error of load
@app.route('/', methods=['GET'])
def welcome():
	data = {
		'info': 'welcome please follow the app documentation to proceed',
		'status': 201
	}
	return jsonify(data)

@app.route('/api', methods=['GET'])
def api_route():
	data = {
		'info': 'you are close, add a version to proceed',
		'status': 201
	}
	return jsonify(data)

# register a blueprint for the version
# with the API standard
app.register_blueprint(sys_app, url_prefix="/api/v1")
