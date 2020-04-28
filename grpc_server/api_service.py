from grpc_server.api_service_pb2 import RatingRequest, RatingReply
from grpc_server.api_service_grpc import APIServiceBase
from grpc_server.util.graphs import get_rating_graph_file

class APIService(APIServiceBase):
    async def GetRating(self, stream):
        request: RatingRequest = await stream.recv_message()
        file = await get_rating_graph_file(handles=request.handles)
        #message = f'I got {len(request.handles)} handles.'
        await stream.send_message(RatingReply(file=file))
