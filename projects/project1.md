# Projekt #1: Profile pracowników

Celem projektu jest stworzenie serwisu do trzymania profili pracowników.

## Spec
Serwis powinien on zawierać wszystkie stałe cechy pracownika przydatne w firmie takie jak:
* Imię
* Nazwisko
* Stanowisko

Dodatkowo:

* Znane języki programowania
* Projekty
* Zespół
* Zdjęcie

## API

### List

```http
GET /employees/
```

### Dodawanie

```http
POST /employees/
```

### Podgląd

```http
GET /employee/id/
```

### Edycja

```http
PUT /employee/id/
```

### Usuwanie

```http
DELETE /employee/id/
```

