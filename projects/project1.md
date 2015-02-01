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

```request
GET /profiles/
```

### Dodawanie

```request
POST /profiles/
```

### Podgląd

```request
GET /profile/id/
```

### Edycja

```request
PUT /profile/id/
```

### Usuwanie

```request
DELETE /profile/id/
```


## Extra

* pobieranie najbliższych urlopów pracownika
* pobieranie kiedy pracownik ostatni raz miał dyżur
