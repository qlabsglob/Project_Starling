from logging import log
from flask import Blueprint, request, jsonify
import datetime

# logger = Blueprint('logger', __name__, template_folder='<template/location>')
communication = Blueprint('communication', __name__)

@communication.route("/comm/postReq", methods=["POST"])
def CommpostReq():
        return jsonify("Communication Post Request Response")

@communication.route("/comm/getReq", methods=["GET"])
def CommgetReq():
    return jsonify(" Communication Get Request  Response")
