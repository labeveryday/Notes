from flask import Flask
import socket
from MySQLdb import connect

# searches for the IP address of the current application container
# displays the IP address in the output of the HTTP request
ip = socket.gethostbyname(socket.gethostname()) 

def get_routers():
    db = connect(host='172.20.0.200', db='inventory')
    c = db.cursor()
    c.execute("SELECT * FROM routers")
    return c.fetchall()

app = Flask(__name__)

@app.route('/')
def home():
    out = (
	f'Welcome to Cisco DevNet.<br>'
        f'IP addresss of the server is {ip}.<br><br>'
    )
    out += 'List of routers in the inventory:<br>'
    for r in get_routers():
        out += f'-> Hostname: {r[0]}; IP: {r[1]}<br>'
    return out

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

