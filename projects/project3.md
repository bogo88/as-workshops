Głosowanie na dzisiejszy obiad
==============================

Projekt ma ułatwić podejmowanie decyzji 'co dziś na obiad'.

Spec
----

Każdy z użytkowników (imię i nazwisko) mogą danego dnia dodać max trzy propozycje obiadu na dany dzień.
Każdy może oddać głos na jedno z dań które danego dnia zostały dodane.

Api
---

Głosowanie
~~~~~~~~~~

```http
GET /vote
```

Oddanie głosu
~~~~~~~~~~~~~

```http
POST /vote/id/
```

Formularz opcji głosowania
~~~~~~~~~~~~~~~~~~~~~~~~~~

```http
GET /create/
```

Stworzenie nowej opcji głosowania (dziś)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```http
POST /create/
```

Wyniki ankiety
~~~~~~~~~~~~~~

```http
GET /results/data/
```

Extra
-----

* Użytkownik może zmienić głos
* Użytkownik może zmienić głos, ale tylko do godz 12
* Dodatkowy opis opcji głosowania (np link do menu)
