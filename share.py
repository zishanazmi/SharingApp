# Import necessary modules

# For implementing the HTTP web servers
import http.server

# Provides access to the BSD secket interface
import socket

# A framework for network servers
import socketserver

# To display a web based document to users
import webbrowser

# TO generate qrcode
import pyqrcode
from pyqrcode import QRCode

# Convert into png format
import png

# TO access operating system control
import os

# Assigning the appropiate port value
PORT = 8010
# This finds the name of the computer user
os.environ['USERPROFILE']

# Changing the directory to access the files desktop with the help of os module
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive')
os.chdir(desktop)

# Creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under which python interpreter is executed
hostname = socket.gethostname()

# Finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

# Converting the IP address into the form of a qrcode with the help of pyqrcode module

# COnverts the IP address into a qrcode
url = pyqrcode.create(link)
# saves the qrcode inform of svg
url.svg("myqr.svg", scale=8)
# Opens the QRCode image in the web browser
webbrowser.open('myqr.svg')

# Creating the HTTP request and serving the folder in the PORT 8010, and the qrcode is generated

# Continous stream of the data between client and server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your browser", IP)
    print("or user the QRCode")
    httpd.serve_forever()



