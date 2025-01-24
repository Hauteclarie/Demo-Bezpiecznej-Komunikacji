# Demo-Bezpiecznej-Komunikacji
Ten projekt demonstruje wykorzystanie szyfrowania do bezpiecznej komunikacji oraz analizuje podatności na ataki, takie jak SQL Injection, wraz z ich zabezpieczeniami.

Funkcje

1. Szyfrowanie za pomocą AES

Cel: Zabezpieczenie wiadomości przesyłanych między użytkownikami.

Algorytm: AES (Advanced Encryption Standard) w trybie CBC z paddingiem PKCS7.

Użycie: Użytkownicy mogą szyfrować i odszyfrowywać wiadomości za pomocą endpointów /encrypt i /decrypt.

2. Podatność na SQL Injection i jej zapobieganie

Demonstracja:

Endpoint /sql_injection_demo celowo jest podatny na atak SQL Injection.

Użytkownicy mogą wprowadzać złośliwe zapytania SQL, aby wykorzystać podatność.

Zapobieganie:

Bezpieczny endpoint /secure_query demonstruje użycie zapytań parametryzowanych w celu zapobiegania atakom SQL Injection.

Struktura plików

app.py

Zawiera aplikację Flask:

Szyfrowanie za pomocą AES.

Demonstracja podatności na SQL Injection oraz bezpieczne zapytania.

templates/index.html

Prosty interfejs frontendowy do interakcji z backendem. Użytkownicy mogą:

Szyfrować i odszyfrowywać wiadomości.

Testować podatność na SQL Injection.

requirements.txt

Lista zależności Pythona:

Flask
cryptography

Endpointy

1. Szyfrowanie wiadomości

URL: /encrypt

Metoda: POST

Dane wejściowe: { "message": "<wiadomość_do_zaszyfrowania>" }

Odpowiedź: { "encrypted": "<zaszyfrowane_w_hex>" }

2. Odszyfrowanie wiadomości

URL: /decrypt

Metoda: POST

Dane wejściowe: { "encrypted": "<zaszyfrowane_w_hex>" }

Odpowiedź: { "decrypted": "<oryginalna_wiadomość>" }

3. Demo SQL Injection

URL: /sql_injection_demo

Metoda: POST

Dane wejściowe: { "input": "<dane_użytkownika>" }

Odpowiedź: Wynik podatnego zapytania.

4. Bezpieczne zapytanie

URL: /secure_query

Metoda: POST

Dane wejściowe: { "input": "<dane_użytkownika>" }

Odpowiedź: Wynik bezpiecznego zapytania.

Jak uruchomić

Sklonuj repozytorium:

git clone <repository_url>
cd <repository_folder>

Ustaw środowisko:

python3 -m venv venv
source venv/bin/activate  # Na Windows: venv\Scripts\activate
pip install -r requirements.txt

Uruchom aplikację:

python app.py

Uzyskaj dostęp do aplikacji:
Otwórz http://127.0.0.1:5000 w przeglądarce.

Dokumentacja

Algorytm szyfrowania: AES

Tryb: CBC (Cipher Block Chaining).

Padding: PKCS7 w celu dopasowania wiadomości do rozmiaru bloku.

Rozmiar klucza: 128-bitowy.

IV (Wektor inicjalizujący): Losowo generowany dla każdej sesji.

Podatność: SQL Injection

Opis: Wykorzystuje niewalidowane dane wejściowe do wykonania dowolnych poleceń SQL.

Demonstracja:

Wejście: ' OR 1=1 --

Wynik: Pobiera wszystkie rekordy z bazy danych.

Zabezpieczenie:

Użycie zapytań parametryzowanych w celu bezpiecznego przetwarzania danych wejściowych użytkownika.
