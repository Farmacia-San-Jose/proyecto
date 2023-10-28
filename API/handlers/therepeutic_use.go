package handlers

import (
	"encoding/json"
	"fmt"
	"net/http"

	"pharmacy_sanjose.com/go/rest-ws/models"
)

func GetTherepeuticUses(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Se obtiene el listado completo de Uso Terapeutico")
}

func GetTherepeuticUse(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	therepeutic_usse := models.TherepeuticUse{Id: 1, TypeTherepeuticuse: "DSA", Description: "dsadsa"}
	output, _ := json.Marshal(&therepeutic_usse)
	fmt.Fprintf(w, ""+string(output))
}

func CreateTherepeuticUse(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Se crea un nuevo Uso Terapeutico")
}

func UpdateTherepeuticUse(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Se actualiza un Uso Terapeutico")
}

func DeleteTherepeuticUse(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Se elimino un registro de Uso Terapeutico")
}
