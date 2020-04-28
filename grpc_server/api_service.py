from grpc_server.api_service_pb2 import RatingRequest, RatingReply
from grpc_server.api_service_grpc import APIServiceBase

class APIService(APIServiceBase):
    async def GetRating(self, stream):
        request: RatingRequest = await stream.recv_message()
        message = f'I got {len(request.handles)} handles.'
        await stream.send_message(RatingReply(file=message))
