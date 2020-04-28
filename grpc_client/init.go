package grpc_client

import (
	"os"

	"google.golang.org/grpc"
)

var Client APIServiceClient

func init() {
	conn, err := grpc.Dial(os.Getenv("GRPC_SERVER_ADDR"), grpc.WithInsecure())
	if err != nil {
		panic(err)
	}
	Client = NewAPIServiceClient(conn)
}