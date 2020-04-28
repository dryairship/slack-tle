import asyncio

from grpclib.utils import graceful_exit
from grpclib.server import Server
from grpclib.reflection.service import ServerReflection

from grpc_server.api_service import APIService
from grpc_server.util import codeforces_api as cf

async def main(*, host='127.0.0.1', port=50051):
    await cf.initialize()
    services = ServerReflection.extend([APIService()])
    server = Server(services)
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
