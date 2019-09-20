from flask import Flask, jsonify

from .routes.router import sys_app

app = Flask(__name__)

# capturing error of load
@app.route('/', methods=['GET'])
def welcome():
	data = {
		'success': 'welcome please follow the documentation spec',
		'status': 201
	}
	return jsonify(data)

# register a blueprint for the version
# with the API standard
app.register_blueprint(sys_app, url_prefix="/api/v1")
