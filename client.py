import grpc
import node_pb2, node_pb2_grpc

def run():
    server_port = 10000
    server_host = 'localhost'
    root_certs = open('ca.pem', 'rb').read()
    priv_key = open('client-key.pem', 'rb').read()
    cert_chain = open('client.pem', 'rb').read()
    credentials = grpc.ssl_channel_credentials(root_certs, priv_key, cert_chain)
    channel = grpc.secure_channel(server_host + ':' + str(server_port), credentials)
    stub = node_pb2_grpc.NodeStub(channel)

    # Test that our successfully connects to the grpc server and can execute
    # a basic "getinfo" command.
    req = node_pb2.GetinfoRequest() 
    resp = stub.Getinfo(req)

    print("Getinfo response: ", resp)

if __name__ == '__main__':
    run()
