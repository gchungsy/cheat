from flask import Flask
from flask_restful import Api, Resource
import time

app = Flask(__name__)
api = Api(app)

class HealthCheck(Resource):
    def get(self):
        return {"status": "ok", "timestamp": time.time()}

class CheatSheet(Resource):
    def get(self, command):
        usage = {
            "nmap": "nmap is a network scanning tool. Usage: nmap [options] [target]",
        }
        return {command: usage.get(command, "No usage information available.")}

api.add_resource(HealthCheck, '/healthz')
api.add_resource(CheatSheet, '/cheat/<string:command>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
