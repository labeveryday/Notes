# Flask Notes

[Find more documentation here](https://flask.palletsprojects.com/en/1.1.x/)

Here's an example of a simple flask app

```python
# Import the Flask class
from flask import Flask
import socket
from MySQLdb import connect

ip = socket.gethostbyname(socket.gethostname())

def get_routers():
    db = connect(host='172.20.0.200', db='inventory')
    c = db.cursor()
    c.execute("SELECT * FROM routers")
    return c.fetchall()

# Create a flask instance
app = Flask(__name__)

# This decorator tells Flask what URL should trigger the function
@app.route('/')
def home():
    out = (
        f'Welcome to Cisco DevNet.<br>'
        f'IP address of the server is {ip}.<br><br>'
    )
    out += 'List of routers in the inventory:<br>'
    for r in get_routers():
        out += f'-> Hostname: {r[0]}; IP: {r[1]}<br>'
    return out

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
```

Notes continued from Knox cbtnuggets training. 

```python
import json
import os
import logging
from flask import Flask, request, jsonify
from flask.logging import create_logger

# Instantiates Flask app
app = Flask(__name__)
# Creates log
LOG = create_logger(app)

# Find the local directory for logs
script_dir = os.path.dirname(os.path.realpath(__file__))

# Create the log file and format
logging.basicConfig(filename=f'{script_dir}\\AppLogs.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Level of info and prints the directory
LOG.info(f"***My Script Directory***: {script_dir}")

# Level of info and prints the database directory
LOG.info(f"DB file: {script_dir}\db.txt")

# GET Request
# Root directory When the go to http://localhost:5000/
@app.route('/')
def index():
    return jsonify({"name": "Du'An",
                    "email": "duanl@labeveryday.com",
                    "locale": "www.labeveryday.com"})

# GET Request
# Routers directory When the go to http://localhost:5000/routers?hostname=SW1 or http://localhost:5000/routers
@app.route('/routers', methods=['GET'])
def getRouter():
    try:
        hostname = request.args.get('hostname')
        print(hostname)
        with open(f'{script_dir}\\db.txt', 'r') as file:
            data = file.read()
            records = json.loads(data)
            if hostname != None:
                for record in records:
                    if record['hostname'] == hostname:
                        LOG.info('Routers returned')
                        return jsonify(record), 200
                    else:
                        return jsonify("No entry found"), 404
            else:
                LOG.warning('Routers returned')
                return jsonify(records), 200
    except Exception as err:
        LOG.error(f'Error during GET {err}')
        return jsonify({"error": err}), 401


@app.route('/routers', methods=['POST'])
def addRouter():
    try:
        # API POST data sent to API
        record = json.loads(request.data)
        print(record)
        LOG.info(f'inbound record {record}')
        # Open db.txt and load it into a JSON object
        with open(f'{script_dir}\\db.txt', 'r') as file:
            data = file.read()
            records = json.loads(data)
        # Checks to see if the post data is in  the db.txt
        if record in records:
            return jsonify({"status": "Device alreaady exists"}), 200
        if record not in records:
            records.append(record)
            LOG.info(f"records output {records}")
            LOG.warning(f"router added {record['hostname']}")
        with open(f"{script_dir}\\db.txt", "w") as file:
            file.write(json.dumps(records, indent=2))
        return jsonify(records), 201
    except Exception as err:
        LOG.error(f"Error during ADD {err}")
        return jsonify({"erro": err})

@app.route('/routers', methods=['DELETE'])
def deleteRouter():
    try:
        # API POST data sent to API
        record = json.loads(request.data)
        print(record)
        LOG.info(f'inbound record {record}')
        # Open db.txt and load it into a JSON object
        with open(f'{script_dir}\\db.txt', 'r') as file:
            data = file.read()
            records = json.loads(data)
        # Checks to see if the post data is in  the db.txt
        if record in records:
            records.remove(record)
            LOG.info(f"records output {records}")
            LOG.warning(f"router delete {record['hostname']}")
        elif record not in records:
            return jsonify("Router not in list. Nothing to remove"), 200
        with open(f"{script_dir}\\db.txt", "w") as file:
            file.write(json.dumps(records, indent=2))
        return jsonify("Router has been removed", records), 201
    except Exception as err:
        LOG.error(f"Error during DELETE {err}")
        return jsonify({"erro": err})
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```