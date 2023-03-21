from flask import Flask
from flask import request
server = Flask(__name__)

@server.route("/", methods = ['GET', 'POST', 'DELETE'])
def hello():
    return request.form

if __name__ == "__main__":
   server.run(host='0.0.0.0')