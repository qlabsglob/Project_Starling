from logging import log
from flask import Blueprint, request, jsonify
import datetime

# logger = Blueprint('logger', __name__, template_folder='<template/location>')
databaseApi = Blueprint('databaseApi', __name__)

@databaseApi.route("/comm/postReq", methods=["POST"])
def DatabaseApiReq():
        return jsonify("Communication Post Request Response")

@databaseApi.route("/comm/getReq", methods=["GET"])
def DatabaseApiReq():
    return jsonify(" Communication Get Request  Response")

# @databaseApi.route("/databaseApi/")