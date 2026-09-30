---
title: Alapfogalmak és strukturált programozás
description: Adat, kifejezés, utasítás, állapot és strukturált programozás
author: Bence Kovács
marp: true
math: mathjax
paginate: true
footer: Prog1 – Alapfogalmak és strukturált programozás
size: 16:9
theme: uncover
style: |
  section {
    background: #fafafa;
    color: #242a33;
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-size: 30px;
    line-height: 1.38;
    letter-spacing: 0;
    padding: 48px 64px 82px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    text-align: left;
  }
  h1, h2, h3 { color: #244c68; letter-spacing: 0; }
  h1 { font-size: 58px; line-height: 1.15; }
  h2 { font-size: 42px; line-height: 1.2; margin: 0 0 28px; }
  h3 { font-size: 32px; margin: 12px 0; }
  p { margin: 0 0 18px; }
  ul, ol { margin: 0 0 18px; padding-left: 1.25em; }
  li { margin: 8px 0; }
  strong { color: #244c68; }
  table { width: 100%; font-size: 27px; border-collapse: collapse; margin: 10px 0 20px; }
  th, td { padding: 14px 16px; text-align: left; border-bottom: 1px solid #bac5cd; }
  th { background: #eaf0f4; color: #244c68; }
  section.title { justify-content: center; text-align: center; }
  section.title h1 { margin-bottom: 28px; }
  section.title h2 { font-size: 52px; }
  section.definition { justify-content: center; text-align: center; }
  section.definition h2 { font-size: 52px; margin-bottom: 40px; }
  section.definition p { font-size: 40px; line-height: 1.45; max-width: 1000px; margin: 0 auto; }
  section.compact { font-size: 28px; }
  section.compact table { font-size: 26px; }
  section.compact th, section.compact td { padding: 9px 14px; }
  section footer {
    position: absolute; left: 64px; bottom: 25px;
    width: auto; padding: 0; margin: 0;
    font-size: 17px; color: #66737f; text-align: left;
  }
  section::after {
    content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
    position: absolute; right: 64px; bottom: 25px;
    padding: 0; font-size: 17px; color: #66737f;
    background: none; text-shadow: none;
  }
  pre { font-size: 27px; line-height: 1.35; padding: 20px 24px; margin: 10px 0 22px; background: #edf1f4; border-radius: 0; box-shadow: none; text-align: left; }
  code { font-family: "DejaVu Sans Mono", monospace; letter-spacing: 0; }
  section.reveal table { font-size: 25px; }
  section.reveal th, section.reveal td { padding: 11px 12px; }
  section.reveal td:first-child { white-space: nowrap; }
  section footer { font-size: 16px; }
  section.expression tbody tr:nth-child(3) { background: #e0ebf2; }
  section.reveal table { font-size: 24px; }
  section.reveal th, section.reveal td { padding: 8px 10px; }
---

<!-- _class: title -->

# Alapfogalmak és strukturált programozás

Adat, kifejezés, utasítás, állapot

---

## Programozási probléma megoldási terve

- **Specifikáció:** mi a feladat, és milyen eredményt fogadunk el?
- **Adat:** milyen információkra van szükségünk?
- **Algoritmus:** milyen lépésekkel állítjuk elő az eredményt?

---

<!-- _class: definition -->

## Adat

A program által tárolható és feldolgozható információ reprezentációja.

---

## Az adat értéke és típusa

- Az adat lehet bemenet, köztes eredmény vagy kimenet.
- A **típus** meghatározza a lehetséges értékeket és a megengedett műveleteket.
- Az **érték** az adott konkrét tartalom.
- Adatokra **nevekkel is hivatkozhatunk**, de nem minden adatnak van saját neve.

Példák Pythonban: `42`, `3.5`, `"alma"`, `True`.

<!-- Pythonban az objektumnak van típusa. A nevek objektumokra hivatkoznak; ugyanahhoz az objektumhoz több név is tartozhat. -->

---

## Adat elnevezése

Az algoritmusban betöltött szerep alapján:

- **Konstans:** a feladat során rögzítettnek tekintett érték.
- **Változó:** a futás során más értéket is hozzárendelhetünk.

```python
MAX_PROBALKOZAS = 3
probalkozas = 0
```

Pythonban a nagybetűs név **konvenció**, nem tiltja az új értékadást.

---

## Nevek Pythonban

- Beszédes név: `osszpontszam`, `maradek`, `ervenyes`.
- Változóknál szokásos forma: `kisbetus_nev` (**snake_case**).
- Konstansoknál szokásos forma: `NAGYBETUS_NEV`.
- A név nem kezdődhet számjeggyel, és nem lehet foglalt szó.
- A kis- és nagybetű különbözik: `pont` és `Pont` két név.

Az ékezet nélküli neveket a példákban következetesen használjuk.
Pythonban az ékezetes azonosítók is megengedettek, de kerülendő a használatuk.

---

## Alapvető adattípusok

| Adattípus                                 | Python-típus | Példa           |
| ----------------------------------------- | ------------ | --------------- |
| Egész szám (integer)                      | `int`        | `42`, `-3`, `0` |
| Lebegőpontos szám (floating-point number) | `float`      | `2.5`, `1e3`    |
| Szöveg (string)                           | `str`        | `"alma"`, `"A"` |
| Logikai érték (boolean)                   | `bool`       | `True`, `False` |

A típus megvizsgálható: `type(42)` eredménye az `int` típus.

---

<!-- _class: expression -->

## Kifejezés

Olyan nyelvi elem, amelynek **sikeres kiértékelése egy értéket eredményez**.

| Kifejezés      | Mit használ?                                            |
| -------------- | ------------------------------------------------------- |
| `42`           | Közvetlenül a kódba írt értéket: **literált (literal)** |
| `pont`         | Egy nevet                                               |
| **`pont + 5`** | **Nevet, literált és operátort**                        |
| `len("alma")`  | Függvényhívást                                          |

---

<!-- _class: reveal -->

## Kifejezések Pythonban (1/7)

A / jellel elválasztott lehetőségek programnyelvfüggők.

| Kód     | Típus | Érték | Megjegyzés |
| ------- | ----- | ----- | ---------- |
| `3 + 4` | ?     | ?     | ?          |

>

---

<!-- _class: reveal -->

## Kifejezések Pythonban (2/7)

A / jellel elválasztott lehetőségek programnyelvfüggők.

| Kód       | Típus | Érték | Megjegyzés |
| --------- | ----- | ----- | ---------- |
| `3 + 4`   | `int` | `7`   |            |
| `2 + 2.5` | ?     | ?     | ?          |

---

<!-- _class: reveal -->

## Kifejezések Pythonban (3/7)

A / jellel elválasztott lehetőségek programnyelvfüggők.

| Kód       | Típus          | Érték        | Megjegyzés                        |
| --------- | -------------- | ------------ | --------------------------------- |
| `3 + 4`   | `int`          | `7`          |                                   |
| `2 + 2.5` | `float` / hiba | `4.5` / hiba | Különböző típusok! Python: `4.5`. |
| `4 > 2`   | ?              | ?            | ?                                 |

---

<!-- _class: reveal -->

## Kifejezések Pythonban (4/7)

A / jellel elválasztott lehetőségek programnyelvfüggők.

| Kód       | Típus          | Érték        | Megjegyzés                        |
| --------- | -------------- | ------------ | --------------------------------- |
| `3 + 4`   | `int`          | `7`          |                                   |
| `2 + 2.5` | `float` / hiba | `4.5` / hiba | Különböző típusok! Python: `4.5`. |
| `4 > 2`   | `bool`         | `True`       |                                   |
| `4 = 2`   | ?              | ?            | ?                                 |

---

<!-- _class: reveal -->

## Kifejezések Pythonban (5/7)

A / jellel elválasztott lehetőségek programnyelvfüggők.

| Kód       | Típus          | Érték        | Megjegyzés                             |
| --------- | -------------- | ------------ | -------------------------------------- |
| `3 + 4`   | `int`          | `7`          |                                        |
| `2 + 2.5` | `float` / hiba | `4.5` / hiba | Különböző típusok! Python: `4.5`.      |
| `4 > 2`   | `bool`         | `True`       |                                        |
| `4 = 2`   | hiba           | hiba         | Értékadás, nem összehasonlítás (`==`). |
| `4 == 2`  | ?              | ?            | ?                                      |

---

<!-- _class: reveal -->

## Kifejezések Pythonban (6/7)

A / jellel elválasztott lehetőségek programnyelvfüggők.

| Kód           | Típus          | Érték        | Megjegyzés                             |
| ------------- | -------------- | ------------ | -------------------------------------- |
| `3 + 4`       | `int`          | `7`          |                                        |
| `2 + 2.5`     | `float` / hiba | `4.5` / hiba | Különböző típusok! Python: `4.5`.      |
| `4 > 2`       | `bool`         | `True`       |                                        |
| `4 = 2`       | hiba           | hiba         | Értékadás, nem összehasonlítás (`==`). |
| `4 == 2`      | `bool`         | `False`      |                                        |
| `4 == "négy"` | ?              | ?            | ?                                      |

---

<!-- _class: reveal -->

## Kifejezések Pythonban (7/7)

A / jellel elválasztott lehetőségek programnyelvfüggők.

| Kód           | Típus          | Érték          | Megjegyzés                             |
| ------------- | -------------- | -------------- | -------------------------------------- |
| `3 + 4`       | `int`          | `7`            |                                        |
| `2 + 2.5`     | `float` / hiba | `4.5` / hiba   | Különböző típusok! Python: `4.5`.      |
| `4 > 2`       | `bool`         | `True`         |                                        |
| `4 = 2`       | hiba           | hiba           | Értékadás, nem összehasonlítás (`==`). |
| `4 == 2`      | `bool`         | `False`        |                                        |
| `4 == "négy"` | hiba / `bool`  | hiba / `False` | Programnyelvfüggő. Python: `False`.    |

---

## Deklarálás és értékadás

**Általánosan:** egyes nyelvekben előbb deklaráljuk a változót, és a típusát is megadjuk.

**Pythonban:** az egyszerű értékadás egy nevet kapcsol egy objektumhoz.

```python
pont = 3 + 4
```

1. Kiértékeljük a jobb oldalt: az eredmény `7`.
2. A `pont` nevet ehhez az értékhez kötjük.

---

## Számok és szövegek

- A `float` véges pontosságú: sok valós számot csak közelít.
- Pythonban az `int` nem rögzített bitszámú; a rendelkezésre álló memória korlátozza.
- Más nyelvekben külön `float` és `double` típus is lehet.
- Pythonban egyetlen karakter is `str`, nincs külön beépített `char` típus.
- A szöveg kódolása fájlok olvasásakor és írásakor is számít.

---

## Utasítás (statement)

Az imperatív programozás egyik **alapvető végrehajtási egysége**.

- Végrehajtandó műveletet ír le.
- Tipikusan a program állapotát (**state**) változtatja.
- Több fajtája van; eddig az **értékadást** láttuk.

```python
pont = 7
pont = pont + 1
```

A második sor végrehajtása után a `pont` értéke `8`.

---

## Kifejezés vs. utasítás

**„Valami” vs. „csinálj valamit”**

| Python-kód | Jelentés                                  |
| ---------- | ----------------------------------------- |
| `a == 4`   | Kifejezés: igaz-e, hogy `a` értéke 4?     |
| `a = 4`    | Utasítás: rendeljük az `a` névhez a 4-et! |

- A **kifejezés** kiértékelhető egy értékké.
- Az **utasításnak** több fajtája van; tipikusan a program állapotát változtatja.

---

<!-- _class: definition -->

## Állapot

A program által adott pontban elérhető és tárolt információk, a végrehajtás aktuális helyzete.

---

## Állapotér

A példákban az elérhető neveket és a hozzájuk tartozó értékeket követjük.

| Név        | A hivatkozott érték típusa | Érték    |
| ---------- | -------------------------- | -------- |
| `pont`     | `int`                      | `7`      |
| `nev`      | `str`                      | `"Anna"` |
| `ervenyes` | `bool`                     | `True`   |

Ez a táblázat az állapot **egyszerűsített nézete**.

<!-- Pythonban a típus az objektumhoz tartozik. A későbbi függvényeknél külön helyi névterekkel is találkozunk. -->

---

## Állapotváltozás: mit kapunk?

```python
a = 3
b = a + 2
a = 10
```

- Mi az `a` és a `b` értéke az egyes sorok után?
- Változik-e `b`, amikor `a` új értéket kap?

---

## Állapotváltozás: lépésenként

| Végrehajtott utasítás | `a`  | `b`                  |
| --------------------- | ---- | -------------------- |
| `a = 3`               | `3`  | Még nincs definiálva |
| `b = a + 2`           | `3`  | `5`                  |
| `a = 10`              | `10` | `5`                  |

A jobb oldalt az értékadás pillanatában értékeljük ki.

A `b = a + 2` nem hoz létre automatikusan újraszámolt kapcsolatot.

---

## Algoritmus

Egy feladat megoldására szolgáló, **pontosan megadott, végrehajtható lépésekből álló eljárás**.

- Az egyes lépések jelentése egyértelmű.
- Meghatározza a végrehajtás sorrendjét és feltételeit.
- Az itt vizsgált feladatoknál minden megengedett bemenetre véges sok lépés után befejeződik.
- Eredménye megfelel a specifikációnak.

Leírhatjuk szöveggel, pszeudokóddal vagy programnyelven.

---

<!-- _class: title -->

## Strukturált programozás

Szekvencia, elágazás, iteráció

---

## A három alapvető vezérlési szerkezet

Vezérlési szerkezet (**control structure**)

| Szerkezet      | Jelentés                             | Python-példa         |
| -------------- | ------------------------------------ | -------------------- |
| **Szekvencia** | Utasítások egymás utáni végrehajtása | Egymást követő sorok |
| **Elágazás**   | Választás feltétel alapján           | `if`, `elif`, `else` |
| **Iteráció**   | Utasítások ismételt végrehajtása     | `while`, `for`       |

Ezeket egymás után és egymásba ágyazva is használhatjuk.

---

## Szekvencia

Az utasításokat a megadott sorrendben hajtjuk végre.

```python
ar = 1200
darab = 3
fizetendo = ar * darab
print(fizetendo)
```

**Miért számít a sorrend?** Az értéket használat előtt meg kell adnunk.

---

## Elágazás

A feltétel határozza meg, melyik ág fut le.

```python
pont = 60
if pont >= 50:
    print("Sikerült")
else:
    print("Még gyakorolni kell")
```

Ebben az `if–else` szerkezetben pontosan az egyik ág hajtódik végre.

**Mi történik 49, 50 és 60 pont esetén?**

---

## Iteráció: while

A feltételt minden ismétlés előtt megvizsgáljuk.

```python
szamlalo = 3
while szamlalo > 0:
    print(szamlalo)
    szamlalo = szamlalo - 1
```

A kiírt értékek: **3, 2, 1**. A végén `szamlalo == 0`.

## **Mi történne az utolsó sor nélkül?**

## Iteráció: for

Sorban végigjárjuk egy iterálható objektum elemeit.

```python
for nev in ["Anna", "Béla", "Csilla"]:
    print(nev)
```

```python
for i in range(3):
    print(i)
```

A második ciklus **0, 1, 2** értékeket ír ki. A felső határ kimarad.
