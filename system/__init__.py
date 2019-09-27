from flask import Flask, jsonify

from .routes.router import sys_app

app = Flask(__name__)


# capturing error of load
@app.route('/', methods=['GET'])
def welcome():
	data = {
		'info': 'welcome please follow the app documentation to proceed',
		'status': 206
	}
	return jsonify(data), 206


@app.route('/api',  methods=['GET'])
@app.route('/api/', methods=['GET'])
def api_route():
	data = {
		'info': 'you are close, add a version to proceed',
		'status': 206
	}
	return jsonify(data), 206


# Handling of route errors
@app.errorhandler(400)
def bad_request(error):
    """
    Gives error message when any bad requests are made.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print (error)
    return jsonify({'error': '{}!'.format(error),'status':400}), 400


@app.errorhandler(404)
def not_found(error):
    """
    Gives error message when any invalid url are requested.
    Args:
        error (string): 
    Returns:
        Error message.
    """
    print (error)
    return jsonify({'error': '{}!'.format(error),'status':404}), 404


@app.errorhandler(403)
def not_allowed(error):
    """
    Gives error message when a resource is restricted from the user access.
    Args:
        error (string): 
    Returns:
        Error message.
    """
    print (error)
    return jsonify({'error': '{}!'.format(error),'status':403}), 403


# register a blueprint for the version
# with the API standard
app.register_blueprint(sys_app, url_prefix="/api/v1")
