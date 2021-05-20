from flask import Flask, jsonify, request

# initialize our Flask application
app= Flask(__name__)

@app.route("/postReq", methods=["POST"])
def postReq():
        return jsonify("Post Request Response")

@app.route("/getReq", methods=["GET"])
def getReq():
    return jsonify(" Get Request  Response")

@app.route("/", methods=["GET"])
def index():
    return jsonify("Tracker Server")


#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True)
