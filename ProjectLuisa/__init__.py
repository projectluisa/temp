from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import json

from ProjectLuisa import database

app = Flask(__name__)


# get tables from the databases and store each one on an api


@app.route('/api/salmonella', methods=["GET"])
def get_salmonella():
    return jsonify(database.get_salmonella())


@app.route('/api/escherichia', methods=["GET"])
def get_escherichia():
    return jsonify(database.get_escherichia())


@app.route('/api/klebsiella', methods=["GET"])
def get_klebsiella():
    return jsonify(database.get_klebsiella())
