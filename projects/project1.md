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
GET /profiles/
```

### Dodawanie

```http
POST /profiles/
```

### Podgląd

```http
GET /profile/id/
```

### Edycja

```http
PUT /profile/id/
```

### Usuwanie

```http
DELETE /profile/id/
```


## Extra

* pobieranie najbliższych urlopów pracownika
* pobieranie kiedy pracownik ostatni raz miał dyżur
