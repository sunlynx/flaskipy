# coding=utf-8
from flask import Flask, jsonify
from modules import flaskipy_post


app = Flask(__name__)
# Configurations
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    # return "Error Message: {0}".format(error)
    response = {
        'success': False,
        'message': "Error Message: {0}".format(error)
    }

    return jsonify(response), 404

# Routes Register
# register post routers
app.register_blueprint(flaskipy_post)

# # print all of the routes path
# endpoints = [rule.rule for rule in app.url_map.iter_rules()]
# print(endpoints)
