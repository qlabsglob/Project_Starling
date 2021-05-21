import socket
from flask import Flask, request, jsonify

app = Flask(__name__)

data = ""

def socketCollector():
    s = socket.socket()
    s.bind(('', 12345))
    s.listen(2)
    a, addr = s.accept()
    global data
    data = str(addr)
    a.detach()
    s.close()
    return

@app.route("/", methods=["GET"])
def returnSocketInfo():
    global data
    return jsonify(data)

@app.route("/testing", methods=["GET"])
def testing():
    return jsonify("testing done")

if __name__=='__main__':
    app.run(debug=True)
    socketCollector();