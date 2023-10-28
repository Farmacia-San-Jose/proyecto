package repository

import (
	"context"

	"pharmacy_sanjose.com/go/rest-ws/models"
)

type TherepeuticUse interface {
	InsertTherepeuticUse(ctx context.Context, therepeutic_use *models.TherepeuticUse) error
	GetTherepeuticUseId(ctx context.Context, id int64) (*models.TherepeuticUse, error)
	Close() error
}

var implementation TherepeuticUse

func SetRepository(repository TherepeuticUse) {
	implementation = repository

}

func InsertTherepeuticUse(ctx context.Context, therepeutic_use *models.TherepeuticUse) error {
	return implementation.InsertTherepeuticUse(ctx, therepeutic_use)
}

func GetTherepeuticUseId(ctx context.Context, id int64) (*models.TherepeuticUse, error) {
	return implementation.GetTherepeuticUseId(ctx, id)
}

func Close() error {
	return implementation.Close()
}
