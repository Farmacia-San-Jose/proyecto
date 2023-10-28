package database

import (
	"context"
	"database/sql"
	"log"

	_ "github.com/go-sql-driver/mysql"
	"pharmacy_sanjose.com/go/rest-ws/models"
)

type MysqlRepository struct {
	db *sql.DB
}

func NewMysqlRepository(url string) (*MysqlRepository, error) {
	db, err := sql.Open("mysql", url)

	if err != nil {
		return nil, err
	}

	return &MysqlRepository{db}, nil
}

func (repo *MysqlRepository) InsertTherepeuticUse(ctx context.Context, therepeutic_use *models.TherepeuticUse) error {
	_, err := repo.db.ExecContext(ctx, "INSERT INTO classifications_usoterapeutico(type_therepeuticuse, description) VALUES($1,$2)", therepeutic_use.TypeTherepeuticuse, therepeutic_use.Description)
	return err
}

func (repo *MysqlRepository) GetTherepeuticUseId(ctx context.Context, id int64) (*models.TherepeuticUse, error) {
	rows, err := repo.db.QueryContext(ctx, "SELECT id, type_therepeuticuse, description FROM classifications_usoterapeutico WHERE id =$1", id)

	defer func() {
		err = rows.Close()
		if err != nil {
			log.Fatal(err)
		}
	}()
	var therepeutic_use = models.TherepeuticUse{}
	for rows.Next() {
		if err = rows.Scan(&therepeutic_use.Id, &therepeutic_use.TypeTherepeuticuse, &therepeutic_use.Description); err == nil {
			return &therepeutic_use, nil
		}
	}
	if err = rows.Err(); err != nil {
		return nil, err
	}

	return &therepeutic_use, nil
}

func (repo *MysqlRepository) Close() error {
	return repo.db.Close()
}
