import grpc
import os
from concurrent import futures
from yoomoney import Client
from dotenv import load_dotenv
from loguru import logger

from service.proto.api_yoomoney_server.api_yoomoney_server_pb2_grpc import PaymentService, add_PaymentServiceServicer_to_server
from service.proto.api_yoomoney_server.api_yoomoney_server_pb2 import CheckReq, CheckResp, GetURLReq, GetURLResp

from service.check import check
from service.get_url import get_url

load_dotenv(".env")
TOKEN = str(os.getenv("TOKEN"))
RECEIVER = str(os.getenv("RECEIVER"))
PORT = str(os.getenv("PORT"))
logger.info(f"\nTOKEN={TOKEN}\nRECIVER={RECEIVER}\nPORT={PORT}\n")
if TOKEN == None or RECEIVER == None or PORT == None:
    logger.error("TOKEN or RECIVER or PORT is empty")
    exit(0)


class PaymentServer(PaymentService):
    client = Client(token=TOKEN)
    receiver = RECEIVER

    def Check(self, request: CheckReq, context) -> CheckResp:
        logger.debug(f"function Check has been called")
        return CheckResp(Ok=check(client=self.client, label=request.Label))

    def GetURL(self, request: GetURLReq, context) -> GetURLResp:
        logger.debug("function GetURL has been called")
        return GetURLResp(URL=get_url(receiver=self.receiver, label=request.Label, sum=request.Sum))


def main():
    logger.info(f"service is started on port={PORT}")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PaymentServiceServicer_to_server(PaymentServer(), server)
    server.add_insecure_port(f"localhost:{PORT}")
    server.start()
    server.wait_for_termination()


if "__main__" == __name__:
    main()