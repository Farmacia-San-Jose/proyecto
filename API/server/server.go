package server

import (
	"context"
	"errors"
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"pharmacy_sanjose.com/go/rest-ws/database"
	"pharmacy_sanjose.com/go/rest-ws/repository"
)

type Config struct {
	Port        string
	JWTSecret   string
	DatabaseURL string
}

type Sever interface {
	Config() *Config
}

type Broker struct {
	config *Config
	router *mux.Router
}

func (b *Broker) Config() *Config {
	return b.config
}

func NewServer(ctx context.Context, config *Config) (*Broker, error) {
	if config.Port == "" {
		return nil, errors.New("Puerto es requerido")
	}
	if config.JWTSecret == "" {
		return nil, errors.New("Secreto es requerido")
	}
	if config.DatabaseURL == "" {
		return nil, errors.New("Database url es requerido")
	}

	broker := &Broker{
		config: config,
		router: mux.NewRouter(),
	}
	return broker, nil
}

func (b *Broker) Start(binder func(s Sever, r *mux.Router)) {
	b.router = mux.NewRouter()
	binder(b, b.router)
	repo, err := database.NewMysqlRepository(b.config.DatabaseURL)
	if err != nil {
		log.Fatal(err)
	}
	repository.SetRepository(repo)

	log.Println("Iniciando el servidor en el puerto", b.Config().Port)

	if err := http.ListenAndServe(b.config.Port, b.router); err != nil {
		log.Fatal("ListenAndServe:", err)
	}
}
