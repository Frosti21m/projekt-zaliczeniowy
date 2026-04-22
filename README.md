# Projekt Zaliczeniowy – Kalkulator Finansowy

## Opis projektu
Aplikacja konsolowa napisana w języku Python, służąca do wykonywania podstawowych obliczeń finansowych.  
Program umożliwia obliczanie przyszłej wartości inwestycji, obliczanie rat kredytowych, generowanie harmonogramu spłat, przeliczanie walut oraz zapisywanie historii operacji do pliku.

## Funkcjonalności
- obliczanie wartości przyszłej inwestycji:
  - procent prosty
  - procent składany
- kalkulator kredytowy:
  - rata miesięczna
  - harmonogram spłat
- przelicznik walut
- zapis historii obliczeń do pliku
- menu konsolowe

## Struktura projektu
- `src/` – moduły aplikacji
- `tests/` – testy jednostkowe
- `data/` – pliki pomocnicze, np. historia i kursy walut
- `main.py` – punkt wejścia do programu

## Wykorzystane klasy
- `Investment`
- `Loan`
- `CurrencyConverter`
- `HistoryManager`

## Obsługa błędów
Program obsługuje nieprawidłowe dane wejściowe, takie jak:
- ujemne kwoty,
- niepoprawne oprocentowanie,
- nieznane waluty,
- błędny format pliku JSON,
- nieprawidłowe dane wpisane przez użytkownika w menu.

## Wymagania
- Python 3.10+
- pytest

## Instalacja i uruchomienie
1. Utwórz i aktywuj środowisko wirtualne.
2. Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt