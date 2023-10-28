package models

type TherepeuticUse struct {
	Id                 int64  `json:"id"`
	TypeTherepeuticuse string `json:"type_therepeuticuse"`
	Description        string `json:"description"`
}
