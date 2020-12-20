# SOE-ProgAlap1-Beadando-Blackjack-Ujvari

A program egy egyszerű BlackJack játékot mutat be.

## A játékos a következő menüpontok közül választhat:
```
Press 1: Hit
Press 2: Stay
Press 3: Exit
Press 4: Save
```
## 1. Hit
Az 1-es gomb megnyomása után a játékos egy véletlenszerű lapot kap egy előre megadott listából. Ez a lap lehet 2-estől 10-ig, vagy jumbó (J), dáma (Q), király (K), ász (A).

A játék célja az, hogy az általunk kapott lapok összege nagyobb legyen az osztó lapjainak összegénél (közelebb legyen a 21-hez). Ha ez az összeg pont 21, akkor nyertünk, ugyanis Blackjackünk van. Viszont ha az összeg nagyobb mint 21, akkor vége a játéknak, ugyanis besokalltunk ("BUSTED!").

## 2. Stay
Ha úgy gondoljuk, hogy nem akarunk több lapot kapni, nehogy besokalljunk, akkor meg tudunk állni. A szabály szerint az osztónak 17-nél mindenképpen meg kell állnia, ezt nevezzük Soft 17-nek.

## 3. Exit
Ha a hármas gombot választjuk, egyszerűen ki tudunk lépni a játékból.

## 4. Save
A négyes gombot választva a játékeredményt, azaz a lapokat egy listában és azok összegét ki tudjuk menteni egy json fájlba.


## A lapok értékei a Blackjack játékban:
- 2–10-ig a kártyák annyit érnek, amennyi a névértékük.
- A bubi, Dáma és Király értéke 10.
- Az ász értéke lehet 1 vagy 11, amelyik előnyösebb a kéz szempontjából. Ha 11-gyel a lapok összege már nagyobb lenne 21-nél, akkor az ász értéke 1, egyébként 11.

