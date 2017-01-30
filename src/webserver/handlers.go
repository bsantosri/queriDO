package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"

	"github.com/gorilla/mux"
)

func Index(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	fmt.Fprintln(w, "Welcome!")
}

func TodoIndex(w http.ResponseWriter, r *http.Request) {
	todos := Todos{
		Todo{Name: "Write presentation"},
		Todo{Name: "Host meetup"},
	}
	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	w.WriteHeader(http.StatusOK)

	if err := json.NewEncoder(w).Encode(todos); err != nil {
		panic(err)
	}
}

func TodoShow(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	todoId := vars["todoId"]
	w.WriteHeader(http.StatusOK)
	fmt.Fprintln(w, "Todo show:", todoId)
}

func GetDocument(w http.ResponseWriter, r *http.Request) {

	type Configuration struct {
		COLLECTORS_PATH []string
	}

	file, _ := os.Open("config.json")
	decoder := json.NewDecoder(file)
	configuration := Configuration{}
	err := decoder.Decode(&configuration)
	if err != nil {
		log.Fatal("error:", err)
	}

	vars := mux.Vars(r)
	ediParam := vars["ediParam"]
	matParam := vars["matParam"]
	w.WriteHeader(http.StatusOK)

	if len(configuration.COLLECTORS_PATH) == 0 {
		log.Fatal("error: varible COLLECTORS_PATH not set")
	}
	python_path := configuration.COLLECTORS_PATH[0]
	script := python_path + "getMateria.py"
	arg1 := fmt.Sprintf("--edition=%v", ediParam)
	arg2 := fmt.Sprintf("--document=%v", matParam)
	out, err := exec.Command("python", script, arg1, arg2).Output()
	if err != nil {
		log.Fatal(err)
	}

	output := fmt.Sprintf("%q\n", out)
	materias := Materias{
		Materia{Edition: ediParam, Document: matParam, Text: output},
	}
	w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	w.WriteHeader(http.StatusOK)
	if err := json.NewEncoder(w).Encode(materias); err != nil {
		panic(err)
	}
}
