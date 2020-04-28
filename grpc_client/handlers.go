package grpc_client

import (
	"context"
	"time"
)

func HandleRating(handles []string) (string, error) {
	request := RatingRequest{Handles:handles}
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	response, err := Client.GetRating(ctx, &request)
	if err != nil {
		return "", err
	}
	return response.File, nil
}