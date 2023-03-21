from flask import Flask
from flask import request
import boto3
from boto3.dynamodb.conditions import Attr, Key, And
server = Flask(__name__)

dynamodb2 = boto3.resource('dynamodb', region_name='us-east-2')
usersTable = dynamodb2.Table('test-microservices');

@server.route("/", methods = ['GET', 'POST', 'DELETE'])
def hello():
    print(request.form)
    response = usersTable.query(
        KeyConditionExpression=Key('id').eq(request.form['id']))

    return response

if __name__ == "__main__":
   server.run(host='0.0.0.0')