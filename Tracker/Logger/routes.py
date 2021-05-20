from logging import log
from flask import Blueprint, request, jsonify
import datetime

# logger = Blueprint('logger', __name__, template_folder='<template/location>')
logger = Blueprint('logger', __name__)

@logger.route("/postReq", methods=["POST"])
def postReq():
        return jsonify("Post Request Response")

@logger.route("/getReq", methods=["GET"])
def getReq():
    return jsonify(" Get Request  Response")

@logger.route("/", methods=["GET"])
def index():
    return jsonify("This is a tracker Server for the ")
