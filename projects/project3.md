# Zapisy na obiad

Celem projektu jest stworzenie aplikacji do zapisów na obiady.

## Cele

* Tworzenie lunch'u: dzień i danie
* Zapisy pracownika na dany lunch
* podsumowanie lunchu na dany okres czasu (ile zapisanych osób)
* podsumowanie lunchu dla pracownika na dany okres czasu


## API

### List
```http
GET /lunch/
```
Query:
* zakres dat
* głodomory

### Create
```http
POST /lunch/
```

### Detail
```http
GET /lunch/<id>/
```

### Subscribe
```http
POST /lunch/<id>/hungry/
```

### Unsubscribe
```http
DELETE /lunch/<id>/hungry/<employee>/
```

