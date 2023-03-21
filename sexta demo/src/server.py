from flask import Flask
from flask import request
import boto3
server = Flask(__name__)

dynamodb2 = boto3.resource('dynamodb', region_name='us-east-2')
usersTable = dynamodb2.Table('test-microservices');

@server.route("/", methods = ['GET', 'POST', 'DELETE'])
def hello():
    usersTable.put_item(
            Item={
                'id':  request.form.id,
                'nombre':   request.form.nombre,
                'whatsapp': request.form.whatsapp,
            })

    return request.form

if __name__ == "__main__":
   server.run(host='0.0.0.0')