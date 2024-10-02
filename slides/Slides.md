---
title: Alapfogalmak, Struktúrált programozás
description: Alapfogalmak, Struktúrált programozás
author: Bence Kovács
marp: true
math: mathjax
class: lead
paginate: false
footer: Prog1
size: 16:9
theme: uncover
---

## Alapfogalmak, Struktúrált programozás

---

### Programozási probléma megoldási terve

- Mi oldja meg a problémát (Specifikáció)
- Mire van ehhez szükség (Adat)
- Hogyan használjuk ezeket a szükséges dolgokat (Algoritmus)

---

### Adat

Minden amit külvilágból leképezve számítógépen tárolunk

---

### Adat

- adatnak van:
  - típusa
  - értéke
  - ha eltároljuk, van neve
- típus meghatározza:
  - értékkészletet
  - elvégezhető műveleteket

---

### Adat elnevezése

Algoritmusban betöltött szerep alapján

Attól függően, hogy egy programban hogyan használjuk az adatot, lehet

- konstans (python: NAGY_NYOMTATOTT)
  - értéke nem változhat a programban
  - π-től fix szövegű hibaüzenetig lehet bármi
- változó (python: no_ekezet)
  - nem feltétlen bemenet (de lehet bemenet)
  - értéke változhat

---

### Elemi adattípusok

- Szám
  - Valós (féle) (float/double)
  - Egész (integer)
- Szöveg (string)
  - nem mindenhol azonos string/char
  - kódolás számíthat
- Logikai (boolean)

---

### Kifejezés

- Kiértékelhető: ugyanúgy értéke és típusa van.
- Konstansokon és/vagy változókon elvégzett műveletek (operációk) elvégzésével lehet kiértékelni
- Rénézésre konstansok/változók és operátor(ok)

---

| Kifejezés | Típus | Érték | Probléma |
| --------- | ----- | ----- | -------- |
| 3 + 4     |       |       |          |

---

| Kifejezés | Típus | Érték | Probléma |
| --------- | ----- | ----- | -------- |
| 3 + 4     | egész | 7     |          |
| 2 + 2.5   |

---

| Kifejezés | Típus      | Érték    | Probléma           |
| --------- | ---------- | -------- | ------------------ |
| 3 + 4     | egész      | 7        |                    |
| 2 + 2.5   | float/hiba | 4.5/hiba | különböző típusok! |
| 4 > 2     |

---

| Kifejezés | Típus      | Érték    | Probléma           |
| --------- | ---------- | -------- | ------------------ |
| 3 + 4     | egész      | 7        |                    |
| 2 + 2.5   | float/hiba | 4.5/hiba | különböző típusok! |
| 4 > 2     | logikai    | igaz     |                    |
| 4 = 2     |

---

| Kifejezés | Típus      | Érték    | Probléma                            |
| --------- | ---------- | -------- | ----------------------------------- |
| 3 + 4     | egész      | 7        |                                     |
| 2 + 2.5   | float/hiba | 4.5/hiba | különböző típusok!                  |
| 4 > 2     | logikai    | igaz     |                                     |
| 4 = 2     | hiba       | hiba     | értékadás, nem összehasonlítás (==) |
| 4 == 2    |

---

| Kifejezés   | Típus      | Érték    | Probléma                            |
| ----------- | ---------- | -------- | ----------------------------------- |
| 3 + 4       | egész      | 7        |                                     |
| 2 + 2.5     | float/hiba | 4.5/hiba | különböző típusok!                  |
| 4 > 2       | logikai    | igaz     |                                     |
| 4 = 2       | hiba       | hiba     | értékadás, nem összehasonlítás (==) |
| 4 == 2      | logikai    | Hamis    |                                     |
| 4 == "négy" |

---

| Kifejezés   | Típus        | Érték      | Probléma                            |
| ----------- | ------------ | ---------- | ----------------------------------- |
| 3 + 4       | egész        | 7          |                                     |
| 2 + 2.5     | float/hiba   | 4.5/hiba   | különböző típusok!                  |
| 4 > 2       | logikai      | igaz       |                                     |
| 4 = 2       | hiba         | hiba       | értékadás, nem összehasonlítás (==) |
| 4 == 2      | logikai      | Hamis      |                                     |
| 4 == "négy" | hiba/logikai | hiba/HAMIS | programnyelve válogatja             |

---

### Hogyan hozunk létre névvel, típussal és értékkel rendelkező adatot?

1. Deklarálás
   - adat nevét megadjuk
   - egyes programnyelveknél típusát
2. Értékadás
   - egyenlőségjel jobb oldalán lévő kifejezést kiértékeljük
   - értékét hozzárendeljük a deklarált névhez

---

### Mi kell ahhoz, hogy létrehozzuk az adatot?

### Utasítás (Statement)

- legkisebb imperatív programozási elem
- program állapotát (state) változtatja
- kategorizálható
- blokkosítható

---

### Kifejezés vs Utasítás

a == 4
a = 4
valami vs csinálj valamit

- Kifejezés kiértékelhető egy értékké
- Utasításból több fajta van, a program állapotát változtatja
  - deklaráció
  - értékadás
  - függvénydefiníció/meghívás
  - ...

---

### Állapot

Minden, a program által adott pontban elérhető és általa tárolt információ.

---

### Állapot keret

Az általunk értelmezett állapotban egy keret jellemezhető egy három oszlopos táblázattal:

| Név (identifier) | Micsoda | Érték/tartalom |
| ---------------- | ------- | -------------- |
| ...              | ...     | ...            |

---

### Algoritmus

Olyan utasítás(sorozat), amely valamely felmerült probléma megoldására alkalmas.

---

## Strukturált programozás

- elágazás
  - if
  - else-if
  - switch/case
- iteráció
  - while
  - for
  - do-while/until
- blokk
  - függvény
  - procedúra

---

### Strukturált programozás

- elágazás
  - feltétel
  - ág
- iteráció
  - feltétel
  - ciklusmag
- blokk
  - utasítássorozat
