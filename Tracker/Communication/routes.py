from logging import log
from flask import Blueprint, request, jsonify
import datetime

# logger = Blueprint('logger', __name__, template_folder='<template/location>')
communicaiton = Blueprint('communication', __name__)

@communicaiton.route("/comm/postReq", methods=["POST"])
def CommpostReq():
        return jsonify("Communication Post Request Response")

@communicaiton.route("/comm/getReq", methods=["GET"])
def CommgetReq():
    return jsonify(" Communication Get Request  Response")
