### 
# Тут тесты только для моего аккаунта,
# они не будут работать с другими аккаунтами.
###

import grpc
from service.proto.api_yoomoney_server.api_yoomoney_server_pb2 import CheckReq, CheckResp
from service.proto.api_yoomoney_server.api_yoomoney_server_pb2 import GetURLReq, GetURLResp
from service.proto.api_yoomoney_server.api_yoomoney_server_pb2_grpc import PaymentServiceStub
from dotenv import load_dotenv
import os

# Проверка на правильный лейбл
def test_check_1():
    load_dotenv()
    port = os.getenv("PORT")
    print(f"PORT:{port}")
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = PaymentServiceStub(channel=channel)
    label = "test01"
    message = CheckReq(Label=label)
    resp = stub.Check(message)
    return resp.Ok
print(test_check_1() == True)

# Проверка на неправильный лейбл
def test_check_2():
    load_dotenv()
    port = os.getenv("PORT")
    print(f"PORT:{port}")
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = PaymentServiceStub(channel=channel)
    label = "test02"
    message = CheckReq(Label=label)
    resp = stub.Check(message)
    return resp.Ok
print(test_check_2() == False)

# Проверка на получение урла
def test_get_url():
    load_dotenv()
    port = os.getenv("PORT")
    print(f"PORT:{port}")
    channel = grpc.insecure_channel(f"localhost:{port}")
    stub = PaymentServiceStub(channel=channel)
    label = "test02"
    message = GetURLReq(Label=label, Sum=150)
    resp = stub.GetURL(message)
    return resp.URL
url = test_get_url()
print("http" in url)
print(url)
