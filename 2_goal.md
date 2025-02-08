# Úloha 2: Goal Programming

## Problém:
Firma XYZ vyrábí dva produkty, A a B, s využitím dvou zdrojů, pracovních hodin a surovin.
Výroba produktu A vyžaduje 5 pracovních hodin a 2 jednotky surovin na kus a výroba produktu B
10 pracovních hodin a 3 jednotky surovin na kus. K dispozici je 300 pracovních hodin a 120
jednotek surovin.

Firma se snaží splnit následující cíle. Cíl zisku je dosáhnout alespoň 8 000 Kč zisku. Přitom zisk na
jednotku produktu A je 100 Kč a zisk na jednotku produktu B je 200 Kč. Cíl výroby je vyrobit
alespoň 30 jednotek produktu A a 20 jednotek produktu B.

Formulujte problém jako úlohu pro goal programming. Definujte rozhodovací proměnné, cíle a
odchylkové proměnné. Řešení nalezněte libovolnou metodou. V jeho rámci uveďte hodnot
rozhodovacích proměnných (počet jednotek A a B k výrobě), odchylky od každého cíle a informaci,
zda šly všechny cíle splnit.

## Definice rozhodovacích proměnných:

- x1 – počet vyrobených jednotek produktu A
- x2 – počet vyrobených jednotek produktu B

## Formulace cílů a odchylkových proměnných:

### Cíl zisku
- 100*x1* + 200*x2* + *d1_mminus* = 8000
- *d1_minus* - nedosažení cíle zisku
### Cíl výroby produktu A:
- *x1* + *d2_minus* = 30
- *d2_minus* - nedosažení cíle výroby A
### Cíl výroby produktu B:
- *x2* + *d3_minus* = 20
- *d3_minus* - nedosažení cíle výroby B
## Formulace omezení zdrojů:
### Pracovní hodiny: 
- 5*x1* + 10*x2* ≤ 300
### Suroviny: 
- 2*x1* + 3*x2* ≤ 120
## Cílová funkce:
- Minimalizovat Z = d1- + d2- + d3-
## Doménové omezení:
- *x1*, *x2*, *d1_minus*, *d2_minus*, *d3_minus* ≥ 0

## Řešení úlohy:

- Jelikož nebyly stanoveny váhy pro jednotlivé cíle, byla použita Archimedeova metoda s váhou 1 pro všechny cíle.
- Pro nalezení optimálního řešení byl použit skript [goal.py](/2_goal.py), který využívá knihovnu PuLP.

## Výsledek:

- Status: Optimal
- Optimální hodnota cílové funkce: 2005.0
###
- Dosažený zisk: 6000.0
- d1_minus = 2000.0
###
- x1 = 30.0
- d2_minus = 0.0
###
- x2 = 15.0
- d3_minus = 5.0
###
- Pracovní hodiny: 300.0
- Spotřeba surovin: 105.0

## Závěr:

- Pro optimální řešení bylo vyrobeno 30 jednotek produktu A a 15 jednotek produktu B.