# SOE-ProgAlap1-Beadando-Blackjack-Ujvari

A program egy egyszerű BlackJack játékot mutat be.

## A játékos a következő menüpontok közül választhat:
```
Options:
1: Hit
2: Stay
3: Current result to a json file and exit
```
## 1. Hit
Az 1-es gomb megnyomása után a játékos egy véletlenszerű lapot kap egy előre megadott listából. Ez a lap 2-estől 10-es értékig terjed, vagy jumbó (J), dáma (Q), király (K), ász (A) lehet.

A játék célja az, hogy a kapott lapjaink összege nagyobb legyen az osztó lapjainak összegénél (közelebb legyen a 21-hez). Ha ez az összeg pont 21, akkor nyertünk, ugyanis Blackjackünk van. Viszont ha az összeg nagyobb mint 21, akkor vége a játéknak, ugyanis besokalltunk ("BUSTED!").

## 2. Stay
Ha úgy gondoljuk, hogy nem akarunk több lapot kapni, nehogy besokalljunk, akkor meg tudunk állni. A szabály szerint az osztónak 17-nél mindenképpen meg kell állnia, ezt nevezzük Soft 17-nek.

## 3. Current result to a json file and exit
Ha a hármas gombot választjuk, akkor a jelenlegi befejezetlen játékeredményt ki tudjuk iratni a `saved.json` fájlba, majd egyszerűen ki tudunk lépni a játékból.

## Ha a játéknak vége
Minden játék végén az eredmény hozzáfűzödik a `blackjack.log` fájlhoz. Ha meg szeretnénk nézni a statisztikát, hányszor nyertünk -ebből hányszor  blackjackkel-, illetve hányszor vesztettünk -ebből hányszor bustedoltunk-, akkor azt a `stat.py` programban tudjuk megnézni.

## A lapok értékei a Blackjack játékban:
- 2–10-ig a kártyák annyit érnek, amennyi a névértékük.
- A bubi, a dáma és a király értéke 10.
- Az ász értéke lehet 1 vagy 11, amelyik előnyösebb a kéz szempontjából. Ha 11-gyel a lapok összege már nagyobb lenne 21-nél, akkor az ász értéke 1, egyébként 11.

