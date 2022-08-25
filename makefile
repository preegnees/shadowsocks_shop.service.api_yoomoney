.SILENT:

run:
	python server.py

test:
	python test_server.py

proto:
	python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. service/proto/api_yoomoney_server/api_yoomoney_server.proto