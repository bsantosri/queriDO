package main

type Materia struct {
	Edition  string `json:"edition"`
	Document string `json:"document"`
	Text     string `json:"text"`
}

type Materias []Materia
