### Just a smol python client

For https://github.com/ElementsProject/lightning/tree/master/cln-grpc

To use, move the `ca.pem`, `client-key.pem`, and `client.pem` files into this project directory before running `client.py`.


### To compile protos

Use this command:

`python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. node.proto primitives.proto`


