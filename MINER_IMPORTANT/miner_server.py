HOST = "127.0.0.1"


import threading
from http.server import HTTPServer, CGIHTTPRequestHandler


print("[.] You just opened the server for the miner, this is 100% needed for the miner...")
def createWebServer():
	server_object = HTTPServer(server_address=(HOST, 80), RequestHandlerClass=CGIHTTPRequestHandler)
	server_object.serve_forever()
threading.Thread(target=createWebServer).start()
