# Projekt #1: Urlopy

Celem projektu jest zarządzanie informacją o urlopach pracowników

## Zapisani
* Bogo


## Spec
Serwis powinien dawać możliwość dodawania, usuwania i wyszukiwania dni, w których
pracownik jest niedostępny

Funkcjonalności:
* dodawanie urlopu
* usuwanie urlopu
* edycja urlopu
* wyszukiwanie urlopu po pracowniku
* wyszukiwanie urlopu po dacie


## API

### List

```http
GET /absence/
```

### Dodawanie

```http
POST /absence/
```

### Podgląd

```http
GET /absence/id/
```

### Edycja

```http
PUT /absence/id/
```

### Usuwanie

```http
DELETE /absence/id/
```

