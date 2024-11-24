from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    # Register introspection functions
    server.register_introspection_functions()
    
    # Register function to check divisibility
    def isDivided_function(x, y):
        return x % y == 0
    server.register_function(isDivided_function, 'isDivided_function')

    # Run the server's main loop
    print("Server is running...")
    server.serve_forever()
