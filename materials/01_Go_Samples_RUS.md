#### **Go**
Начинаем с описания моделей. В Go нет привычных в ООП классов и объектов, поэтому описываем структуры.

```go
type ExampleModel {
    ID          string `json:"id"`
    ExampleModelAttr string `json:"example_model_attr"`
}
```

Не забудем импортировать все нужные пакеты.

```go
package main

import (
  "log"
  "net/http"
  "math/rand"
  "strconv"
  "encoding/json"
  "github.com/gorilla/mux"
)
```

Теперь опишем методы, обрабатывающие HTTP запросы. Пусть это будет метод getModels, который получает все модели. На вход методу подаются ResponseWriter и указатель на Request.

```go
var models []models

func getModels(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(models)
}
```

Рассмотрим теперь точку входа.

```go
func main() {
    r := mux.NewRouter();
    ...
    r.HandleFunc("/models", getModels).Methods("GET")
    log.Fatal(http.ListenAndServe(":8000", r))
}
```
